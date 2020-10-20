#!/usr/bin//env python
# -*- coding:utf-8 -*-
import smbus
import time

import RPi.GPIO as GPIO     
from time import sleep
#from pcf8591WithVoltage import PCF8591 as ADC
#from scipy.io import wavfile
    
"""                   
#GPIO.cleanup() 
LedPin = 25   
freq =100                    
dc = 0          

GPIO.setmode(GPIO.BCM)               
GPIO.setup(LedPin, GPIO.OUT)     

pwm = GPIO.PWM(LedPin, freq)     
pwm.start(dc)
"""

address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
Compared = 9
tic=0
tok=0

GPIO.setmode(GPIO.BCM)

INT1 = 11
INT2 = 12



GPIO.setup(INT1,GPIO.OUT)
GPIO.setup(INT2,GPIO.OUT)
status =0 # 0 for IR blocked, 1 for IR reached
try:
    while True:
        bus.write_byte(address,A0)
        tik = time.thread_time()
        value = bus.read_byte(address)
        if value < 50:
            status = 1
        else:
            status =0
        while True:
            bus.write_byte(address,A0)
            value = bus.read_byte(address)
            if value < 50:
                Compared = 1
            else:
                Compared =0
            if status!=Compared:
                tok = time.thread_time()
                #print(tik)
                #print (tok)
                Compared = status
                break

        span = tok - tik
        speedRPM = 1/(40*span)
    
        print("AOUT:%1.3f  " %(speedRPM))
    #value= value **2 /100
except KeyboardInterrupt:
    GPIO.cleanup()

#     pwm.ChangeDutyCycle(0)
