import sys
import os
from time import sleep
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
import argparse
import locale
import logging

from aiy.board import Board, Led

def main():
    machine_on_off = False # default off
    board = Board()
    while True:
        if machine_on_off == True & board.button.wait_for_press(5):
            print('off')
            machine_on_off = False
            board.led.state = Led.OFF
        elif machine_on_off == False & board.button.wait_for_press(5):
            print('on')
            machine_on_off = True
            board.led.state = Led.BLINK

    '''board.led.state = Led.ON
        sleep(1)
        board.led.state = Led.OFF
        sleep(1)
        board.led.state = Led.BLINK
        sleep(10)
        print("BLINK_3")
        board.led.state = Led.BLINK_3
        sleep(10)
        print("BEACON")
        board.led.state = Led.BEACON
        sleep(10)
        print("BEACON_DARK")
        board.led.state = Led.BEACON_DARK
        sleep(10)
        print("PULSE_QUICK")
        Led.PULSE_QUICK
        sleep(10)
        print("PULSE_SLOW")
        Led.PULSE_SLOW'''
def voice_machine_on_off(board, machine_on_off):
    if machine_on_off == False:
        board.led.state = Led.BLINK
    else:
        board.led.state = Led.OFF

if __name__ == '__main__':
    main()