This is a simple Voice Assistant created for simple use like getting time, open any website,Opening google docs, searching topic on Google website, Wikipedia, searching on Youtube.

First step is to install all the requirments - 
   pip install -r requirements.txt
 


The SpeechRecognition library allows Python to access audio from your system’s microphone, transcribe the audio, and save it.

The PyAudio library allows for audio input and output stream.

Google’s text-to-speech package, gTTS converts your audio questions to text. The response from the look-up function that you write for fetching answer to the question is converted to an audio phrase by gTTS. This package interfaces with Google Translate’s API.

Playsound package is used to give voice to the answer. Playsound allows Python to play MP3 files.

Wikipedia is used to fetch a variety of information from the Wikipedia website.

Wolframalpha is a computational knowledge engine or answer engine that can compute mathematical questions using Wolfram’s knowledge base and AI technology. You need to fetch the API to use this package.



After installing requirements type command:
  python3 Zubaan.py
