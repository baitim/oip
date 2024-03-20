import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac,GPIO.OUT)

def dec2bin(x):
        return [int(element) for element in bin(x)[2:].zfill(8)]

try:
    while True:
        print("Input number:")
        num = input()
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print("Voltage = ", voltage)
            else :
                if num < 0:
                    print("input number < 0")
                elif num > 255:
                    print("input number > 255")
        except Exception:
            if num == "q":
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("End")