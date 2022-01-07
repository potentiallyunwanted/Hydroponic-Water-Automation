from machine import Pin, I2C
import time

pump = Pin(26, Pin.OUT)
light = Pin(25, Pin.OUT)


def pump_on():
    light.on()
    pump.on()


def pump_off():
    light.off()
    pump.off()
    
while True:
    pump_on()
    time.sleep(10)
    pump_off()


