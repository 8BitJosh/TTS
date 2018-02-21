import vlc
from gtts import gTTS
import time


class tts:
	def __init__(self):
		self.instance = vlc.Instance("--no-video --aout=alsa")
		self.player = self.instance.media_player_new()

	def play(self, string):
		tts = gTTS(text=string, lang='en')
		tts.save('./file.mp3')

		media = self.instance.media_new('./file.mp3')
		self.player.set_media(media)
		self.player.play()

		time.sleep(0.1)
		while (self.player.get_state() == vlc.State.Playing):
		 	time.sleep(0.1)

proc = tts()

try:
	while True:
		data = input('=>')
		try:
			proc.play(data)
		except:
			pass
except KeyboardInterrupt:
	pass