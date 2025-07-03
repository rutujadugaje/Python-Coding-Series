# Install an External module and use it to perform an operation of your interest

# -> 
# First install following package 
# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Pooja .")
engine.runAndWait()


# This code uses the `pyttsx3` library to convert text to speech. It initializes the text-to-speech engine, converts the text "Hello Pooja ." into speech, and plays it. The `runAndWait()` method is called to ensure that the speech is played before the program exits.
# The `pyttsx3` library is a text-to-speech conversion library in Python. It works offline and is compatible with both Python 2 and 3. It supports multiple TTS engines, including SAPI5 on Windows and NSSpeechSynthesizer on macOS.