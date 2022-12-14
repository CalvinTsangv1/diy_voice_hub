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


from time import sleep, time
import vlc
import os
from threading import Thread
from threading import Event
import alsaaudio

SUPPORTED_FILETYPES = ('wav', 'raw', 'voc', 'au')


class EventListener(object):
    callbacks = None

    def on(self, eventName, callback):
        if self.callbacks is None:
            self.callbacks = {}

        if eventName not in self.callbacks:
            self.callbacks[eventName] = [callback]
        else:
            self.callbacks[eventName].append(callback)

    def trigger(self, name):
        if self.callbacks is not None and name in self.callbacks:
            for callback in self.callbacks[name]:
                callback(self)

class VLCPlayer(EventListener):
    def __init__(self, media_folder_path = None):
        #setup media player
        self.instance = vlc.Instance()
        self.player = vlc.MediaListPlayer()
        self.media_list = self.instance.media_list_new()
        self.media_folder_path = media_folder_path
        self.music_index = 0

        self.sound_mixer = alsaaudio.Mixer()
        self.sound_mixer.setvolume(20)

        self._started = Event()
        self._process = None
        self._media_state = None

    
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
                    print(media)
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

    def play(self, index=0):
        if self.player == None:
            print("Please init media player")
        self.music_index = index
        self.player.play_item_at_index(0)
        sleep(10)
        #self.player.play_item_at_index(self.music_index)
        #self._process = Thread(target=self._play_item)
        #self._process.start()

    def _play_item(self):
        self.player.play_item_at_index(self.music_index)
        self.player.audio_set_volume(100)
        sleep(10000)

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