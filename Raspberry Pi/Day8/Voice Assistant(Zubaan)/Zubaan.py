import speech_recognition as sr 
import datetime
import wikipedia
import requests 
import playsound
from gtts import gTTS 
import os
import wolframalpha 
from selenium import webdriver

def respond(output):
	num = 0
	print(output)
	num+=1
	response=gTTS(text=output, lang='en')

	file = str(num)+".mp3"
	response.save(file)
	playsound.playsound(file, True)
	os.remove(file)

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone(device_index=3) as src:
		#print("Something1")
		r.adjust_for_ambient_noise(src, duration=0.5)
		#r.record(src, duration=2)
		audio = r.listen(src)
		data =""
		#print("Something2")
		try:
			data = r.recognize_google(audio)
			data = data.lower()
			print(data)
		except Exception as e:
			print("Exception: ", str(e))
	return data


if __name__ == '__main__':
	respond("Hi I am Zubaan, your personal desktop assistant.")

while(1):
	respond("How may I help you?")
	text = get_audio()
	if text == 0:
		continue

	if "stop" in str(text) or "exit" in str(text) or "quit" in str(text) or "bye" in str(text) in str(text):
		respond("Ok Bye")
		break

	if 'wikipedia' in text:
		respond("Searching Wikipedia ...")
		text = text.replace("wikipedia", "")
		results = wikipedia.summary(text, sentences= 3)
		respond("According to Wikipedia")
		print(results)
		respond(results)

	elif 'time' in text:
		strTime = 	datetime.datetime.now().strftime("%H:%M:%S")
		respond(f"The time is {strTime}")

	elif 'search' in text:
	
		text = text.replace("search","")
		webbrowser.open_new_tab(text)
		time.sleep(5)

	elif 'calculate' or 'what is' in text :

		question 	= get_audio()
		app_id	 	= "API ID" 
		client		= wolframaplha.Client(app_id)
		res 		= client.query(question)
		answer		= next(res.results).txt
		respond("The answer is" + answer)

	elif "open google" in text:
		webbrowser.open_new_tab("https://www.google.com/")
		respond("google is open")
		time.sleep(5)

	elif 'youtube' in text:
		driver 	= webdriver.Chrome(r'Mention Link')
		driver.implicitly_wait(1)
		driver.maximize_window()
		respond("Opening Youtube")
		indx 	= text.split().index('youtube')
		query 	=text.split()[indx+1:]
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))

	elif "open google docs" in text:
		respond("Opening Google Docs")
		webbrowser.open_new_tab("https://docs.google.com/document/")

	else:
		respond("Query Not Avaliable")