import timeit

start = timeit.timeit()
print("hello")

# from  AudioToTranscript import AudioToTranscript
# from VideoToAudio import VideoToAudio
# from TextToSummary import TextToSummary
# obj1 = VideoToAudio(video_path=r"C:\Users\Admin\Desktop\sighack\zoom-friend\full_lecture.mp4",audio_path=r"./sample_tr.wav")
# obj1.convert()
# obj = AudioToTranscript(audio_filename = "full-lecture-sound.wav")

# print(obj.convertToTranscript())
# obj2 = TextToSummary()
INPUT='''
hello there
'''
INPUT = INPUT[0:4000]
from transformers import pipeline
summarizer = pipeline("summarization")

print(summarizer(INPUT, max_length=200, min_length=100, do_sample=False))

# print(obj2.summarize(INPUT))
end = timeit.timeit()
print(f'TIME TAKEN : {end - start} min ')
