import timeit

start = timeit.timeit()
print("hello")

from  AudioToTranscript import AudioToTranscript
from VideoToAudio import VideoToAudio
# obj1 = VideoToAudio(video_path=r"C:\Users\Admin\Desktop\sighack\zoom-friend\full_lecture.mp4",audio_path=r"./sample_tr.wav")
# obj1.convert()
obj = AudioToTranscript(audio_filename = "full-lecture-sound.wav")

print(obj.convertToTranscript())
end = timeit.timeit()
print(f'TIME TAKEN : {end - start} min ')
