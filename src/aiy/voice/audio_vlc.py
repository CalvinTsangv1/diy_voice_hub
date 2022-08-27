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

from ctypes import sizeof
from time import sleep
import vlc
import os
from threading import Thread
from threading import Event
import alsaaudio

SUPPORTED_FILETYPES = ('wav', 'raw', 'voc', 'au')

class VLCPlayer:
    def __init__(self, media_folder_path = None):
        #setup media player
        self.instance = vlc.Instance()
        self.media = vlc.MediaPlayer()
        self.player = vlc.MediaListPlayer()
        self.media_list = self.instance.media_list_new()
        self.media_folder_path = media_folder_path

        self.sound_mixer = alsaaudio.Mixer()
        self.sound_mixer.setvolume(70)

        self._started = Event()
        self._process = None

    
    def __enter__(self):
        return self

    def __exit__(self):
        print('quit VLC Player!')
        self._process = None
        self._started.clear()
        self.instance = None
        self.player = None
        self.media_list = None
        vlc.quit_app()

    def _load_media_list(self):
        if self._process != None:
            print('running load media list...')
            self._started.wait()
            for file in os.listdir(self.media_folder_path):
                print(str(file))
                if file.split(".")[1] == 'mp3':
                    media = self.instance.media_new(self.media_folder_path + "/" + file)
                    self.media_list.add_media(media)
                else:
                    print('failed to load media file: ' + file)
            self.player.set_media_list(self.media_list)
            print("load media list finished !")
        else:
            print('failed to load media list')

        #clear process thread
        self._process = None
        self._started.clear()

    def get_instance(self):
        if self.get_instance != None & self.player != None:
            return self.player
        return None

    def load_media(self, media_path):
        if media_path != None:
            self.media_folder_path = media_path
        else:
            raise ValueError('media folder path is not setup!')
        
        while self._process != None:
            print('waiting to load media...')
            sleep(1)
        self._process = Thread(target=self._load_media_list)
        self._process.start()
        self._started.set()

    def get_media_list(self):
        if self.media_folder_path == None:
            print("Please load media player")
        
        if self.media_list == None:
            print("Please reload play list")

        return self.media_list.__dict__
    
    def get_media(self, index):
        return self.player.__getitem__(index)

    def play(self, index):
        if self.player == None:
            print("Please init media player")
        self._process = Thread(target=self._play_item, args=(index,))
        self._process.start()
        self._started.set()

    def _play_item(self, index):
        self.player.play_item_at_index(index)
        while self.is_playing():
            self._started.wait(1)
        #clear process thread
        self._process = None
        self._started.clear()
        


    def pause(self):
        if self.player is not None:
            self.player.pause()

    def start(self):
        if self.player is not None:
            self.player.play()

    def next(self):
        if self.player is not None:
            self.player.next()

    def previous(self):
        if self.player is not None:
            self.player.previous()

    def is_playing(self):
        return self.player.is_playing()

    def set_volume(self, number):
        self.media.audio_set_volume(number)