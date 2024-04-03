import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
troyka = 13
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
comp = 14
GPIO.setup(comp, GPIO.IN, )

def dec2bin(value):
    return [int(el) for el in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    num = 0
    for bit in range(7, -1, -1):
        num += 2**bit
        num2dac(num)
        time.sleep(0.01)
        compVal = GPIO.input(comp)
        if compVal == 1:
            num -= 2**bit
    return num

try:
    while(True):
        val = adc()
        volt = float(val)/256*3.3
        print("ADC: value = {}, V = {:.2f}".format(num2dac(val), volt))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print("end")