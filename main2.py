import RPi.GPIO as GPIO
import time
from sensors.waterLevel import get_distance
from sensors.waterFlow import count_pulse, read_flow_lpm
import warnings
import requests
import joblib
import serial
from comm.lcd import display

def warn(*args, **kwargs):
    pass


warnings.warn = warn

# Globals
TRIG = 23
ECHO = 24
FLOW_SENSOR = 17
pulse_count = 0
url = "https://flood-detection-dashboard-9uc3.onrender.com/api/flooddata/receive/"
model = joblib.load("flood_model.pkl")
PORT = "/dev/serial0"
BAUDRATE = 9600
PHONE_NUMBERS = ["7817993226", "8423120404", "9899971463"]
# PHONE_NUMBER = "+917817993226"
MESSAGE = [
    "Flood Alert:\nDANGER\nFlood is near your area",
]

# Initializing sensors
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def send_command(command, delay = 2):
    print(f"\n>>> {command}")
    gsm.write((command + "\r\n").encode())
    time.sleep(delay)
    response = gsm.read_all().decode(errors="ignore")
    print(response)
    
    return response

def sending_sms(message):
    for PHONE_NUMBER in PHONE_NUMBERS:
        print("\nStarting SMS mode...")

        gsm.write(f'AT+CMGS="{PHONE_NUMBER}"\r\n'.encode())

        time.sleep(3)

        response = gsm.read_all().decode(errors="ignore")

        print(response)

        # Wait for > prompt
        if ">" not in response:
            print("Did not receive > prompt")
            exit()
        print("Sending SMS...")

        gsm.write(message.encode())

        time.sleep(1)

        gsm.write(bytes([26]))

        time.sleep(8)

        final_response = gsm.read_all().decode(errors="ignore")

        print("\nFINAL RESPONSE:")
        print(final_response)

        if "OK" in final_response:
            print("\nSMS SENT SUCCESSFULLY")
        else:
            print("\nSMS FAILED")


try:
    gsm = serial.Serial(port=PORT, baudrate=BAUDRATE, timeout=1)
    print("SIM800L connected")
    time.sleep(5)
    response = send_command("AT")
    
    if "OK" not in response:
        print("SIM800L not responding")
    send_command("AT+CPIN?")
    send_command("AT+CSQ")
    send_command("AT+CREG?")
    response = send_command("AT+CMGF=1")
    if "OK" not in response:
        print("Failed to set SMS mode")
except Exception as e:
    print("Error:", e)
init()
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=count_pulse)

try:
    while True:
        distance = f"{get_distance(TRIG, ECHO):.2f}"
        flow = f"{read_flow_lpm():.2f}"

        status = ""
        prediction = model.predict([[distance, flow]])

        if prediction == 0:
            status = "safe"
        elif prediction == 1:
            status = "warning"
        else:
            status = "danger"
            sending_sms(MESSAGE[0])

        data = {"distance": distance, "flow": flow, "status": status}
        try:
            requests.post(url, json=data)
        except:
            pass
        print(data)
        display(f"D: {distance} F: {flow}", f"Status: {status}")
        # print(f"Distance: {dist:.2f} cm, Speed of water: {flow:.2f}L/min")
        time.sleep(1)

except KeyboardInterrupt:
    print("Closing")
finally:
    GPIO.cleanup()
    gsm.close()
