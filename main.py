from VideoToInfo import Clipper, VideoToAudio, TextToSummary, AudioClipToText 
import json   


def convertToInfo(video_filename):
    obj1 = VideoToAudio.VideoToAudio(video_filename=video_filename)
    audio = obj1.convert()
    print(audio)
    obj2 = Clipper.Cliper(audio_filename=audio, number_of_pieces=5)
    clips = obj2.clip()
    print(clips)
    trans = []
    for clip in clips:
        obj3 = AudioClipToText.AudioClipToText(audio_filename=clip)
        tran = obj3.convert()
        print(tran)
        trans.append(tran)
        
    print(trans)
    summ = []
    for tran in trans:
        obj4 = TextToSummary.TextToSummary()
        text = obj4.summarize(tran)
        summ.append(text)
        

    print(summ)
    d = {'summ' : summ, 
            'trans':trans}
    with open("sample.json", "w") as outfile:  
        json.dump(d, outfile) 
    return summ


if __name__ == "__main__":
    print(convertToInfo(r"C:\Users\Admin\Desktop\sighack\zoom-friend-v2\VideoToInfo\file.mp4"))
     