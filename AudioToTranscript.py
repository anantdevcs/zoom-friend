# take an audio file
# if not in wav convert it
# split it need be
# make another class to handle the actual transc
# call the class
# return the results
from mylogger import mylogger
from pydub import AudioSegment
import math
import os
import torch
import torchaudio
from glob import glob
#Thanks mubin986
#https://stackoverflow.com/questions/37999150/how-to-split-a-wav-file-into-multiple-wav-files
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath =  filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')



class WavConverter:
    def __init__(self, audio_filename):
        self.audio_filename = audio_filename

    def convertToWav(self):
        mylogger.info(f'Now in converter converting to wav {self.audio_filename} ')
        if self.audio_filename.endswith('.wav'):
            print("File already in Wav")
            return self.audio_filename
        elif self.audio_filename.endswith('.mp3'):
            mylogger.info('mp3 conversion possible')
            sound = AudioSegment.from_mp3(self.audio_filename)
            new_filename = self.audio_filename.split('.')[0] + '.wav'
            sound.export(new_filename, format='wav')
            mylogger.info('conversion done')
            return new_filename
        else:
            mylogger.error(f'File {self.audio_filename} can not be converted')
            return 'ERROR'
    
    

        

class AudioToTranscript:
    def __init__(self, audio_filename):
        mylogger.info('Started constructing the AudioToTranscript class object')
        self.audio_filename = audio_filename
        if not self.audio_filename.endswith('.wav'):
            mylogger.error('Filename not ends with wav')
            mylogger.info('converting to wav file ')
            wavconv = WavConverter(audio_filename=self.audio_filename)
            self.audio_filename = wavconv.convertToWav()
            mylogger.info('Converison done')
            mylogger.info(f'New file if {self.audio_filename}')

        mylogger.info('checking for size of the file')
        self.all_cut_files = self.getClipFiles()
        mylogger.info(f'all files split {self.all_cut_files}')

    def getClipFiles(self, min_per_split=5):
        mylogger.info('Now clipping')
        audio = AudioSegment.from_file(self.audio_filename)
        duration = audio.duration_seconds
        if duration < 300:
            mylogger.info(f'file too small < 5min')
            return [self.audio_filename]
        try:
            os.mkdir('./temp_audio')
        except :
            mylogger.error('can not create directory')
        clipper = SplitWavAudioMubin(folder='./temp_audio', filename=self.audio_filename)
        clipper.multiple_split(min_per_split=min_per_split)
        mylogger.info('done spliting')
        all_files_created = ['./temp_audio/' + x for x in os.listdir('./temp_audio')]
        mylogger.info(f'trancibed into {all_files_created}')
        return all_files_created
    
    def convertToTranscript(self):
        mylogger.info('started transcibing')
        res = ''
        print(self.all_cut_files)
        mylogger.info(f'{self.all_cut_files}')
        for filename in self.all_cut_files:
            res += self.convertSingle(filename=filename)
        
        print(res)
        return res

    
    def convertSingle(self, filename):
        
        
        mylogger.info(f'started trancribing {filename}')
        device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU

        model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                            model='silero_stt',
                                            language='en', # also available 'de', 'es'
                                            device=device)
        (read_batch, split_into_batches,
        read_audio, prepare_model_input) = utils  # see function signature for details

        # download a single file, any format compatible with TorchAudio (soundfile backend)
        # torch.hub.download_url_to_file('https://opus-codec.org/static/examples/samples/speech_orig.wav',
        #                                dst ='speech_orig.wav', progress=True)
        test_files = glob(filename)
        batches = split_into_batches(test_files, batch_size=10)
        input = prepare_model_input(read_batch(batches[0]),
                                    device=device)

        output = model(input)
        res = ''
        for example in output:
            res += str(decoder(example.cpu()))
        
        return res 