from pydub import AudioSegment
from .mylogger import mylogger


class Cliper:
    def __init__(self, audio_filename, number_of_pieces) :
        '''
            returns a list of split audio_files
        '''
        self.audio_filename = audio_filename
        self.number_of_pieces = number_of_pieces

    def clip(self):
        mylogger.info(f'Trying to clip file specd by {self.audio_filename}')
        sound = AudioSegment.from_mp3(self.audio_filename)
        point_len = len(sound) // self.number_of_pieces
        list_splitted = []
        for i in range(self.number_of_pieces):
            sound_clip = sound[i*point_len : min(len(sound), (i + 1) * point_len)]
            fname = f'splitted_{i}_.mp3'
            mylogger.info(f'splitting into {fname}')
            sound_clip.export(fname, format='mp3')
            list_splitted.append(fname)
        return list_splitted
