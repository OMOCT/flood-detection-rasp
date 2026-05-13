import RPi.GPIO as GPIO
import time

def count_pulse(channel):
    global pulse_count
    pulse_count += 1

def read_flow_lpm(duration_sec=1):
    global pulse_count
    pulse_count = 0
    time.sleep(duration_sec)
    pulses = pulse_count
    flow_lpm = (pulses/450.0) * 60
    return flow_lpm
