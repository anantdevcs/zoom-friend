from mylogger import mylogger
from moviepy.editor import VideoFileClip
# example of logging
# mylogger.debug("bruhhh")


class VideoToAudio:
    def __init__(self, video_path, audio_path):
        self.video_path = video_path
        self.audio_path = audio_path
        mylogger.info(f'Seen {self.video_path} and {self.audio_path}')
    def convert(self):
        mylogger.info('Starting to convert')
        video = VideoFileClip(self.video_path) 
        audio = video.audio 
        audio.write_audiofile(self.audio_path) 
        mylogger.info('Ended conversion')

    def getAudioFile(self):
        return self.audio_path