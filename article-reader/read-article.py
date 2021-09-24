import keyboard
import pyttsx3
import requests
from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
for voice in voices:
   engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
def check_key(key):
    if keyboard.read_key() == "esc":
        is_stop = True
        engine.stop()

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  

text = str(input("Paste article\n"))
res = requests.get(text)
soup = BeautifulSoup(res.text, 'html.parser')
articles = []
for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)
text = " ".join(articles)
speak(text)
# engine.save_to_file(text, 'test.mp3') ## If you want to save the speech as a audio file
engine.runAndWait()


is_stop = False

while not is_stop:
    check_key(keyboard.read_key())
