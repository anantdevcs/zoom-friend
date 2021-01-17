# Zoom Friend
### Zoom Friend is an AI powered tool for automatically generating the transcript, summary and sample questions from any of your recorded class lectures. 

## ✈️ Getting started
### Prerequisites

1.  [Git](https://git-scm.com/downloads).
2.  [Python 3.6](https://www.python.org/downloads/)
3.  [Pip3](https://pypi.org/project/pip)
4.  Zoom Friend uses [Voice Gain](https://www.voicegain.ai/) for performing audio to text conversion. So you will need to generate a JWT token in order to use this service

### Installation

1. `git clone` this reposotory.
1. `cd` to `zoom-friend` directory' 
1.  Run `pip install -r requirements.txt` from the terminal. This will install the required python packages
1. Generate your [Voice Gain](https://www.voicegain.ai/) JWT token and insert it in ``VideoToInfo/AudioClipToText.py`` file
1.  Run `python app.py`. This will run a localhost  flask server on your machine. Copy the url of the localhost and run it on your favourite web browser!
1. You might be prompted to download some NLTK packagesas well as some transformer models. 

### References 
Special thanks to https://github.com/patil-suraj/question_generation and https://github.com/huggingface/transformers