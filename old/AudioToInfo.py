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
        self.audio_filename = "heyyyy" + '.mp3'

    def convert(self):
        start = timeit.timeit()
        tran = '''
        he what you're looking at is a hermetically sealed glass laboratory scientists here are engineering special chips that could power the next computing revolution a universal quantum computer chances are you've heard of quantum computers and that they're going to change everything quantum computers have the potential to completely change how we use technology of the teacher the computational power is off the charts what's about to happen with quantum computing is going to make the past look incredibly slow quantum computers are new kinds of machines that promise an exponential growth in processing power capable of tackling problems our computers today can't solve an encryption busting global problem solving quantum computer doesn't exist just yet the field has gained some serious momentum we've reached a point where it's pretty clear that those performance numbers are good enough now you could build a real product a real piece of technology out of this idea and when that threshold got crossed people started to place their beds tech giants like ibm and google and startups like brigade computing are all in something of a scientific race to build the first universal quantum computer but to fully understand what makes a quantum computer so uniquely powerful you'll need to know a bit of quantum mechanics quantum mechanics is the field that describes the simplest things around us individual electrons or atoms or particles of light like photons and the fascinating thing is when you look at these very simple systems they don't really obey the same rules that the world around us does we use sort of two very important properties of quantum mechanics one of them is superposition of states and the other 
one is entanglement when we talk about classical computing we often hear the word bit and bit can refer to zero and one you can also think of it as a binary state you have a switch give me honor can be off for instance when you're physically typing commands into your computer to write an email each letter you strike on the keyboard is translated to a unique string of zeros and ones that are being switched on and off to digitally represent your words
        '''
        # obj1 = VideoToAudio(video_path=self.video_filepath, audio_path=self.audio_filename)
        # obj1.convert()
        # obj2 = AudioToTranscript(audio_filename=self.audio_filename)
        # tran = obj2.convertToTranscript()
        # tran = SpellCorrect(tran)
        # mylogger.info(f'the tran that i recvd is {tran}')

        obj3 = TextToSummary()
        summary = obj3.summarize(text=tran)
        mylogger.info(f'summary i revcd is {summary}')
        end = timeit.timeit()
        print(f'TIME TAKEN : {end - start} min ')

        return {'transcript' : tran,
                'summary' : summary
            }
       
        
    
if __name__ == "__main__":
    obj = AudioToInfo(video_filepath=r"C:\Users\Admin\Desktop\sighack\zoom-friend\file.mp4")
    res = obj.convert()
    with open("sample.json", "w") as outfile:  
        json.dump(res, outfile) 
    
    print(f"FINAL {res}")

