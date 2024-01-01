import tkinter as tk
from googletrans import Translator
import speech_recognition as sr 
from gtts import gTTS 
from googletrans import LANGUAGES
import time as t
# Initialize Translator
translator = Translator()

# Print all languages
for index, (code, lang) in enumerate(LANGUAGES.items()):
    print(f"{index}\t{code}\t\t{lang}")

mic = sr.Microphone()
t.sleep(1)
rec = sr.Recognizer()

# Recognize the words spoken in the audio input
with mic as source:
    # Initialize Translator 
    translator = Translator()
    # Ask user what Language translate
    Lang_1_index = int(input("Which language is your text in? "))
    Lang_2_index = int(input("Which lanuage do you want to translate your code into? "))

    index_to_language = {index: code for index, (code, name) in enumerate(LANGUAGES.items())}

    # Accessing language code using an index 
    desired_language_code1 = index_to_language.get(Lang_1_index)
    desired_language_code2 = index_to_language.get(Lang_2_index)

    print("Please speak now")  
    rec.adjust_for_ambient_noise(source, duration=0.2)
    # Listening
    audio = rec.listen(source)
    rec_aud = rec.recognize_google(audio)

# Print the input audio as text
print("Here is the audio input :" + rec_aud)
to_translate = translator.translate(rec_aud,src= desired_language_code1, dest = desired_language_code2)
translated_text = to_translate.text
print("The translated text is " , translated_text)
