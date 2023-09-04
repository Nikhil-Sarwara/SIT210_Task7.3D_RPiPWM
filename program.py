#Import the DistanceSensor and PWMLED classes from the gpiozero module
from gpiozero import DistanceSensor, PWMLED

#Import the sleep function from the time module
from time import sleep

#Create a DistanceSensor object with echo pin 15 and trig pin 14, and set the maximum distance to 0.4 meters
sensor = DistanceSensor(echo = 15, trig = 14, max_distance = 0.4)

#Create a PWMLED object with pin 18
led = PWMLED(18)

#Define a function to map a value from one range to another
def map(value, start1, end1, start2, end2):
    return (value - start1) * (end2 - start2) / (end1 - start1) + start2 

#Loop Forever
white True:
    ## Get the distance in meters from the sensor and multiply by 100 to get centimeters
    distance = sensor.distance * 100

    ## Print the distance in centimeters
    print("Distance in cm: " + distance)

    ## Set the LED brightness to a value mapped from the distance range (0 to 40 cm) to the PWM range (1 to 0)
    led.value = map(distance, 0, 40, 1, 0)

    ## Wait for one second sleep(1)
    sleep(1)
