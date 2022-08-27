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

    if on_voice_machine(board, machine_on_off) == True:
        machine_on_off = True
        print('machine on')
    elif on_voice_machine(board, machine_on_off) == False:
        machine_on_off = False
        print('machine off')


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

def on_voice_machine(board, machine_on_off):
    while True:
        board.button.wait_for_press()
        reach_on_criteria = board.button.wait_for_release(5)
        if reach_on_criteria == True & machine_on_off == False:
            board.led.state = Led.BLINK
            return True
        if reach_on_criteria == True & machine_on_off == True:
            board.led.state = Led.OFF
            return False
        sleep(1)

if __name__ == '__main__':
    main()