from output_module import output
from process_module import process,LoginDialog
from input_module import take_input
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import time
import sys
from common_fun import *;
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import speech_recognition as sr
import webbrowser
import os
from weather import *;
from database import *;
os.system("cls")

def STT():
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
            return text.lower()
        except Exception as e:
            print(e)
            return "Sorry Speak Again"
        
def ANDRU():
        # wish()
        while True:
            query = STT()
            print('query:',query)
            o = process(query)
            speak(o)
            
            if o == 'exiting personal assistant':
                print('Turning off the personal assistant!!')
                # change_value_of_specified('spotify_control','no')
                break

ANDRU()