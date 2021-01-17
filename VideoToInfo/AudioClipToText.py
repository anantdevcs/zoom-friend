from voicegain_speech import ApiClient
from voicegain_speech import Configuration
from voicegain_speech import TranscribeApi
import base64
from .mylogger import mylogger

class AudioClipToText: 
    '''
        takes an audio clip and convertes to text
    '''
    def __init__(self, audio_filename) :
        self.audio_filename = audio_filename

    def convert(self):
        mylogger.info(f'started the diff part aud fn {self.audio_filename}')
        JWT = "insert your <JWT> here"

        configuration = Configuration()
        configuration.access_token = JWT
        api_client = ApiClient(configuration=configuration)


        transcribe_api = TranscribeApi(api_client)
        file_path = self.audio_filename
        mylogger.info('started a connction')
        with open(file_path, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode()
        print('started a connction 2')
        response = transcribe_api.asr_transcribe_post(
            sync_transcription_request={
                "audio": {
                    "source": {
                        "inline": {
                            "data": audio_base64
                        }
                    }
                }
            }
        )
        mylogger.info('done')
        alternatives = response.result.alternatives
        if alternatives:
            local_result = alternatives[0].utterance
            # mylogger.info("result from file: ", local_result)
            return local_result

        else:
            local_result = None
            mylogger.error("no transcription")
            return "conn fail"



