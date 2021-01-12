from .mylogger import mylogger
from moviepy.editor import VideoFileClip
import moviepy.editor as mp

class VideoToAudio:
    def __init__(self, video_filename):
        '''
            takes a videofilename and fully converts the file to mp3
        '''
        self.video_filename = video_filename
        self.audio_path =  'temp_converted00.mp3'

    def convert(self):
        clip = mp.VideoFileClip(self.video_filename)
        clip.audio.write_audiofile(self.audio_path)
        mylogger.info(f"converted {self.video_filename} to {self.audio_path} ")
        return self.audio_path



