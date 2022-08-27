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
import tempfile
from aiy.board import Board, Led
from aiy.voice.audio import AudioFormat, play_wav, record_file, play_mp3, play_mp3_pause, play_mp3_play, vlcPlayer
from aiy.voice.audio_vlc import VLCPlayer
from aiy.voice.audio import AudioFormat, play_wav, record_file

TEST_SOUND_PATH='/home/pi/sound_list'
TEST_SOUND_PATH_1='/usr/share/sounds/alsa/Front_Center.wav'
ERROR_NO_SPEAKER_SOUND = '''There may be a problem with your speaker. Check that it is connected properly.'''

def main():
    machine_on_off = False # default off
    music_on = False # default off
    board = Board()
    player = VLCPlayer()
    player.load_media(TEST_SOUND_PATH)

    with tempfile.NamedTemporaryFile() as f:
        print('Recording for %d seconds...' % 3)

        record_file(AudioFormat.CD, filename=f.name, filetype='wav',
                    wait=lambda: sleep(3))
        print('Playing back recorded audio...')
        play_wav(f.name)


    '''while True:
        machine_on_off = voice_machine_on_off(board, machine_on_off)
        if machine_on_off:
            player.play_item(0)
            machine_on_off = False'''

def ask(prompt):
    answer = input('%s (y/n) ' % prompt).lower()
    while answer not in ('y', 'n'):
        answer = input('Please enter y or n: ')
    return answer == 'y'

def error(message):
    print(message.strip())

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
    if machine_on_off == True & board.button.wait_for_press():
        board.led.state = Led.OFF
        return False
    if machine_on_off == False & board.button.wait_for_press():
        board.led.state = Led.BLINK
        return True

if __name__ == '__main__':
    main()