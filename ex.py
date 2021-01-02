from  AudioToTranscript import AudioToTranscript
from VideoToAudio import VideoToAudio
# obj1 = VideoToAudio(video_path=r"C:\Users\Admin\Desktop\sighack\zoom-friend\sample-lecture.mp4",audio_path=r"./sam_tr.wav")
# obj1.convert()
obj = AudioToTranscript(audio_filename = "sam_tr.wav")

print(obj.convertToTranscript())