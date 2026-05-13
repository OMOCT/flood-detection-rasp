import RPi.GPIO as GPIO
import time
from sensors.waterLevel import get_distance
from sensors.waterFlow import count_pulse, read_flow_lpm
import warnings
import requests
import joblib
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

# Initializing sensors
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

        data = {
            "distance": distance,
            "flow": flow,
            "status": status
        }
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
