from gpiozero import DistanceSensor, PWMLED
from time import sleep

sensor = DistanceSensor(echo = 15, trig = 14, max_distance = 0.4)
led = PWMLED(18)

def map(value, start1, end1, start2, end2):
    return (value - start1) * (end2 - start2) / (end1 - start1) + start2 

white True:
    distance = sensor.distance * 100
    print("Distance in cm: " + distance)
    led.value = map(distance, 0, 40, 1, 0)
    sleep(1)