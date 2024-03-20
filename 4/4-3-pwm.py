import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
n = 11
GPIO.setup(n,GPIO.OUT)

p = GPIO.PWM(n, 1000)
p.start(0)

try:
    while True:
        x = int(input())
        p.ChangeDutyCycle(x)
        print(3.3*x/1000)
finally:
    p.stop()
    GPIO.output(n, 0)
    GPIO.cleanup()
    print("End")