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


def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('turn on the light',
                'turn off the light',
                'blink the light',
                'goodbye')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    with Board() as board:
        on_voice_machine(board)



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

def on_voice_machine(board):
    reach_on_criteria = board.button.wait_for_release(5)
    if reach_on_criteria == True:
        board.led.state = Led.BLINK
    else:
        board.led.state = Led.ON
        sleep(1)
        board.led.state = Led.OFF

if __name__ == '__main__':
    main()