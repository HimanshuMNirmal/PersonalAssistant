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


lastCommand = []
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)



def shift_left():
    return lastCommand[1:] + lastCommand[:1]

class mainT(QThread):
    
    def __init__(self):
        super(mainT,self).__init__()
    
    def run(self):
        self.ANDRU()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
            global lastCommand
            if len(lastCommand) >5:
                print('d')
                lst = shift_left()
                lst.pop()
                lst.append(text)
                lastCommand = lst
            else:
                lastCommand.append(text)
            return text.lower()
        except Exception as e:
            print(e)
            # speak("Sorry Speak Again")
            return "Sorry Speak Again"
        text = text.lower()
        return text

    def ANDRU(self):
        # wish()
        while True:
            self.query = self.STT()
            print('query:',self.query)
            o = process(self.query)
            speak(o)



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = LoginDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
        "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/new.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()
        self.ts = time.strftime("%A, %d %B")
        # self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
        weather = getWeather('')
        try:
            if '20' in weather:
                self.label_6.setText("<font size=8 color='blue'>"+weather+"</font>")
            elif '35' in weather:
                self.label_6.setText("<font size=8 color='red'>"+weather+"</font>")
            else:
                self.label_6.setText("<font size=8 color='green'>"+weather+"</font>")
            self.label_6.setFont(QFont(QFont('Acens',8)))
        except Exception:
            pass
    
    def setTextOfCommand(self):
        
        self.label_6.setText("<font size=8 color='white'>"+'\n'.join(lastCommand)+"</font>")
        self.label_6.setFont(QFont(QFont('Acens',8)))

    

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())