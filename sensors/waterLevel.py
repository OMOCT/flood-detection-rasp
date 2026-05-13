import time
import RPi.GPIO as GPIO

def get_distance(TRIG, ECHO):
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start, end = 0.0, 0.0
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()

    delta = end - start
    dist = (delta * 34300) / 2
    return dist
