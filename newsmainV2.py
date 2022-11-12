# #install the pyttsx3 ---- pip install pyttsx3
# #install the beautifulsoup4 --- pip install beautifulsoup4
# #install the requests --- pip install requests
# #install the playsound --- pip install playsound
# #install the gTTS(Google text to Speech) --- pip install gTTS

import pyttsx3
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from gtts import gTTS
import os

#To collect all the headings of the news in a List
headings = []

#To loop all the pages of the NDTV site news

for number in range(2, 3):

    #To get the content of the page stored in html_text
    html_text = requests.get(f'https://www.ndtv.com/india/page-{number}').content
    #converting HTML document into data structure
    soup = BeautifulSoup(html_text, 'lxml')
    #finding all the h2 tags in the document and storing in the list
    h2_tag = soup.find_all('h2', class_='newsHdng')

    #finding all the anchor tags present in the h2 tags and extracting the headings
    for h2_tag_element in h2_tag:
        a_tag = h2_tag_element.find('a')
        print(a_tag.text)
        headings.append(a_tag.text + '.' + '\n')

#creating a text file and writing all news headings in the file
file1 = open('demofile.txt', 'w')
file1.writelines(headings)
file1.close()

#this is nominal but I added it to feel like an assitant
#Initiating the pyttsx3
speaker = pyttsx3.init()
#Telling it what to say
speaker.say("Hi Sir, Playing recent news")

#reading the file in which we wrote all the headings and storing text in the variable
#text_to_say
f = open("demofile.txt", "r")
text_to_say = f.read()

#Creating the gTTS object and giving it the text, language, pace
gtts_object = gTTS(text=text_to_say, lang='en', slow=False)
#Saving the mp3 file
gtts_object.save("4news.mp3")
#Running the pyttsx3 --- nominal
speaker.runAndWait()
#playing the mp3 file on the system using playsound module.
playsound("4news.mp3")
#deleting the mp3 file
os.remove("4news.mp3")
