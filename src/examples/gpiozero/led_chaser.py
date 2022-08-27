#!/usr/bin/env python3
"""Demonstrates on board LED support with correct polarity.

Implements simple LED chaser.
"""
import sys
sys.path.append("/home/pi/diy_voice_hub/src")
from time import sleep
from gpiozero import LED
from aiy.pins import (int(PIN_A), int(PIN_B), int(PIN_C), int(PIN_D))

leds = (LED(PIN_A), LED(PIN_B), LED(PIN_C), LED(PIN_D))
while True:
    for led in leds:
        led.on()
        sleep(0.5)
        led.off()
