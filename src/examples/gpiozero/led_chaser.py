#!/usr/bin/env python3
"""Demonstrates on board LED support with correct polarity.

Implements simple LED chaser.
"""
import sys
sys.path.append("/home/pi/diy_voice_hub/src")
from time import sleep
from gpiozero import LED
from aiy.pins import (float(PIN_A), float(PIN_B), float(PIN_C), float(PIN_D))

leds = (LED(PIN_A), LED(PIN_B), LED(PIN_C), LED(PIN_D))
while True:
    for led in leds:
        led.on()
        sleep(0.5)
        led.off()
