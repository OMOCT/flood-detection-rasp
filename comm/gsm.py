import serial
import time

PORT = "/dev/serial0"
BAUDRATE = 9600

PHONE_NUMBERS = ["7817993226", "8423120404", "9899971463"]

MESSAGE = ["Flood Alert:\nWARNING\nFlood may occurn near your area",
           "Flood Alert:\nDanger\nFlood is near your area"]

def send_command(command, delay = 5):
    print(f"\n>>> {command}")
    gsm.write((command + "\r\n").encode())
    time.sleep(delay)
    response = gsm.read_all().decode(errors="ignore")
    print(response)
    
    return response
