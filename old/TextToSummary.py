MAGIC_LEN = 1000
from transformers import pipeline
import time
from mylogger import mylogger

class TextToSummary:
    def __init__(self, lower_ratio=0.1, higher_ratio=0.3):
        self.lower_ratio = lower_ratio
        self.higher_ratio = higher_ratio
        

    def summarize(self, text):
        then = time.time()
        
        summarizer = pipeline("summarization")
        clips = self.clipIfNeeded(text)
        full_summary = ''
        for clip in clips:
            mylogger.info(f'Recieved text len={len(clip)} for summarization {len(clips)} ')
            
            max_length, min_length = int(len(clip) * self.higher_ratio), int(len(clip) * self.lower_ratio)
            print(max_length, min_length, len(clip))
            res = summarizer(clip, max_length=max_length, min_length=min_length , do_sample=False)
            summary_text = res[0]['summary_text']
            mylogger.info(f'summary recvd {len(summary_text)}')
            full_summary += summary_text
        now = time.time()
        mylogger.info(f'Recieved summary {full_summary}')
        mylogger.info(f'Took {now - then} seconds') 
        return full_summary
    
    def clipIfNeeded(self, text):
        return [text[i : i +  MAGIC_LEN] for i in range(0, len(text) - MAGIC_LEN - 1, MAGIC_LEN)] 


