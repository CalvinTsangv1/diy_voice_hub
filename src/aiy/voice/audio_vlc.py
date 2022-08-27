"""
APIs to record and play audio files.

.. note::

    These APIs are designed for the Voice Kit, but have no dependency on the Voice
    HAT/Bonnet specifically. However, many of the APIs require some type of sound card
    attached to the Raspberry Pi that can be detected by the ALSA subsystem.

.. module:: aiy.voice.audio

Playback
--------

.. autofunction:: vlc

Audio format
------------


"""

import vlc
import os
from threading import Thread
from threading import Event

SUPPORTED_FILETYPES = ('wav', 'raw', 'voc', 'au')

class VLCPlayer:
    def __init__(self, media_folder_path = None):
        self.instance = vlc.Instance()
        self._started = Event()
        self.player = vlc.MediaListPlayer()
        self.media_folder_path = media_folder_path
        self.media_list = self.instance.media_list_new()
        self._process = None

    
    def __enter__(self):
        return self

    def __exit__(self):
        print('quit VLC Player!')
        vlc.quit_app()

    def load_media_list(self, media_path):
        print('running')
        print(str(os.listdir(media_path)))
        for file in os.listdir(media_path):
            print(str(file))
            if file.split(".")[1] == 'mp3':
                media = self.instance.media_new(file)
                self.media_list.add_media(media)
            else:
                print('failed to load file: ' + file)
        self.player.set_media_list(self.media_list)
        print("loaded all media list")

    def load_media(self, media_path):
        print('thread create')
        thread = Thread(target=self.load_media_list(media_path))
        thread.start()
        print('thread started')
        self._started.set()