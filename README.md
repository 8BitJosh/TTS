## TextToSpeech player

A program the reads user text input and plays the audio
Requires an internet connection

### Requirements

vlc needs to be installed on the system

python packages to be installed via pip
* gtts
* python-vlc


### For linux install

Install external dependencies
```bash
sudo apt-get install python3-pip vlc-nox
```

Pip python packages
```bash
pip install --user -U -r ./requirements.txt
```

Running
```bash
python3 ./tts.py
```
Then just type in some text and it will say it out loud
Just ```Ctr+c``` to exit