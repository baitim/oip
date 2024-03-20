import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac,GPIO.OUT)

def dec2bin(x):
        return [int(element) for element in bin(x)[2:].zfill(8)]

print("input period:")
period = float(input())
x = 0
inc = 0
try:
    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0:
            inc = 1
        elif x == 255:
            inc = 0

        if inc == 1:
            x = x + 1
        else:
            x = x - 1

        sleep(period / 1000)
except ValueError:
    print("Invalid period")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("End")