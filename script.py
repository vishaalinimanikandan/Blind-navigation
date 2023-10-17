from gtts import gTTS
import os

mytext = "There is a car in front of you!! "
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("test01.mp3")
os.system("mpg321 example.mp3")