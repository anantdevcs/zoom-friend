from  AudioToTranscript import AudioToTranscript
from VideoToAudio import VideoToAudio
from TextToSummary import TextToSummary
from mylogger import mylogger
import timeit 
import os
import uuid 
import json
from SpellCorrector import SpellCorrect


class AudioToInfo:
    def __init__(self, video_filepath) :
        '''
        Takes a video filename and returns the transcript and summary of the video filename
        '''
        self.video_filepath = video_filepath
        self.audio_filename = str(uuid.uuid4()) + '.wav'

    def convert(self):
        start = timeit.timeit()

        obj1 = VideoToAudio(video_path=self.video_filepath, audio_path=self.audio_filename)
        obj1.convert()
        obj2 = AudioToTranscript(audio_filename=self.audio_filename)
        tran = obj2.convertToTranscript()
        tran = SpellCorrect(tran)
        mylogger.info(f'the tran that i recvd is {tran}')
        obj3 = TextToSummary()
        summary = obj3.summarize(text=tran)
        mylogger.info(f'summary i revcd is {summary}')
        end = timeit.timeit()
        print(f'TIME TAKEN : {end - start} min ')

        return {'transcript' : tran,
                'summary' : summary
            }
        
    
if __name__ == "__main__":
    obj = AudioToInfo(video_filepath=r"C:\Users\Admin\Desktop\misc\We’re Close to a Universal Quantum Computer, Here’s Where We're At [720p].mp4")
    res = obj.convert()
    with open("sample.json", "w") as outfile:  
        json.dump(res, outfile) 
    
    print(f"FINAL {res}")

