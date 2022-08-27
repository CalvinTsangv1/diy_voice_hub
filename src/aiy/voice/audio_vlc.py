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
import threading

SUPPORTED_FILETYPES = ('wav', 'raw', 'voc', 'au')

class VlcPlayer:
    def __init__(self, media_folder_path = []):
        if self.instance == None:
            self.instance = vlc.Instance()
        self.media_folder_path = media_folder_path
        self._process = None
        self._started = threading.Event()
    
    def __enter__(self):
        return self

    def __exit__(self):
        print('quit VLC Player!')
        vlc.quit_app()

    def load_media_list(self, media_path):
        self._started.wait()
        for file in os.listdir(media_path):
            if file.split(".")[1] == 'mp3':
                self.media_list.insert(file)
            else:
                print('failed to load file: ' + file)
        print("loaded all media list")

    def load_media(self, media_path):
        thread = threading.Thread(target=load_media_list, args=(self, media_path))
        thread.start()
        self._started.set()