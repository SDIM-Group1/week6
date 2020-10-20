# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

INT1 = 11
INT2 = 12

ENA = 16


GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)

pwma = GPIO.PWM(16,80)
pwma.start(90)
GPIO.output(INT1,GPIO.HIGH)
GPIO.output(INT2,GPIO.LOW)

try:
    while 1:
        pwma.ChangeDutyCycle(90)
        time.sleep(3)
        pwma.ChangeDutyCycle(10)
        time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()