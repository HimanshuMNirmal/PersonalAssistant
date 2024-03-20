from output_module import output
from time_details import get_time
from database import *;
from internet import check_internet_connection,check_on_wikipedia
from weather import *;
import time;
from common_fun import *;
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from spotify_control import *;
import pygetwindow as gw
import pyautogui as pag
import subprocess
from num2words import num2words
from whatsapp_automate import *;
import imp

# Specify the file path
module_file_path = r'H:\Personal Assistant\gesture_module\hand-gesture-recognition-mediapipe-main\hand-gesture-recognition-mediapipe-main\app.py'

# Load the module
module = imp.load_source('module_name', module_file_path)

def process(query):

    answer = get_value_from_memory(query)
    if (get_value_of_specified('spotify_control') == 'no'):
        if answer == "get time details":
            return ("Time is "+ get_time())
        
        elif answer == "get internet connectivity":
            if check_internet_connection():
                return ("Internet is connected")
            else:
                return ("Internet is not connected")
        
        elif answer == "get wikipedia":
            ans = check_on_wikipedia(query)
            return (ans if ans!=False else "Didnt find anything on wikipedia")
        
        elif answer == 'get the temperature':
            
            return (getWeather(query))
        
        elif answer == 'youtube search':

            query = query.replace('in','')
            query = query.replace('search','')
            query = query.replace('on','')
            query = query.replace('youtube','')
            query = query.replace('this','')
            query = query.replace('find','')
            search_link(f'https://www.youtube.com/results?search_query={query}')
            return ("searched in youtube")

        elif answer == 'browser search':
            query = query.replace('in','')
            query = query.replace('search','')
            query = query.replace('on','')
            query = query.replace('browser','')
            query = query.replace('this','')
            query = query.replace('find','')
            search_link(f'https://www.google.com/search?q={query}')
            return ("searched in browser")
        
        elif answer == 'current date':
            strDate = datetime.datetime.now().strftime("%d - %m - %Y")
            print("\nDate is: ",strDate)
            newDate = strDate.split(' - ')
            newD = ""
            for i in range(len(newDate)):
                newD += num2words(int(newDate[i]))
                newD +=' '
            return(newD)
        
        elif answer == 'current day':
            current_datetime = datetime.datetime.now()
            day_of_week = current_datetime.weekday()

            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            current_day = days_of_week[day_of_week]

            return current_day

        elif answer == 'open drive':
            
            query = query.replace('search','')
            query = query.replace('open','')
            query = query.replace('drive','')
            query = query.replace('on','')
            query = query.replace('my','')
            query = query.replace('computer','')
            query = query.replace('pc','')
            query = query.replace('laptop','')
            query = query.replace('from','')
            return open_drive(query)
        
        elif answer == 'close window':
            pag.hotkey('Alt','f4')
            return 'window closed'
        
        elif answer == 'go to tab':
            query = find_number(query)
            print('tab:' ,query)
            # query = query.replace('go')
            pag.hotkey('Ctrl',str(query[0]))

        elif answer == 'last page':
            pag.hotkey('ctrl','shift','t')
            return 'opening last tab'
        
        elif answer == 'close tab':
            number = find_number(query)
            if len(number)!=0:
                pag.hotkey('ctrl',str(number[0]))
            pag.hotkey('Ctrl','w')
            return 'Tab closed'
        
        elif answer == 'next tab':
            pag.hotkey('Ctrl','tab')

        elif answer == 'prev tab':
            pag.hotkey('Ctrl','shitft','tab')

        elif answer == 'next video':
            pag.hotkey('shift','n')
            return 'starting next video'
        
        elif answer == 'stop video' or answer == 'start video':
            pag.press('k')
        
        elif answer == 'youtube history':
            search_link('https://www.youtube.com/feed/history')
        
        elif answer == 'remember task':
            pass
        
        elif answer == 'remembered task':
            pass
        
        elif answer == 'send wp msg':
            speak("Enter number and message:")
            number = input("Phone Number:")
            message = input("Message")
            time = input("Time:")
            send_whatsapp_message(f'+91{number}', message, time)
            return 'Message scheduled successfully'
        
        # elif answer == 'switch to spotify':

        #     change_value_of_specified('spotify_control','yes')
        #     return 'switching to spotify mod'

        elif answer == 'gesture mod':
            speak('switching to Gesture mod')
            module.main()
            speak('exiting from gesture mod')
        elif answer == 'exit PS':

            change_value_of_specified('spotify_control','no')
            return 'exiting personal assistant'

            """
            elif answer == "play song":
                try:
                    spotify_windows = gw.getWindowsWithTitle("Spotify Free")
                    if spotify_windows:
                        # If Spotify window exists, bring it to the foreground
                        spotify_windows[0].activate()
                        # print("Spotify window is already open. Focused on Spotify.")
                    else:
                        # If Spotify window doesn't exist, open Spotify application
                        subprocess.Popen(['spotify'])
                        # print("Spotify app is not running. Opened Spotify.")
                    
                    time.sleep(.5)
                    if is_icon_present('lib\playIcon.png'):
                        pag.press('space')
                    else:
                        pass
                        # print("Icon not found in screenshot.")
                except Exception as e:
                    pass
            """
        # else:
        #     return ("Nothing to return  " )
    else:
        print('in spotify')
        if answer == "play song":
            try:
                spotify_windows = gw.getWindowsWithTitle("Spotify Free")
                if spotify_windows:
                    # If Spotify window exists, bring it to the foreground
                    spotify_windows[0].activate()
                    # print("Spotify window is already open. Focused on Spotify.")
                else:
                    # If Spotify window doesn't exist, open Spotify application
                    subprocess.Popen(['spotify'])
                    # print("Spotify app is not running. Opened Spotify.")
                
                time.sleep(.5)
                if is_icon_present('lib\playIcon.png'):
                    pag.press('space')
                else:
                    pass
                    # print("Icon not found in screenshot.")
            except Exception as e:
                pass

        elif answer == "pause song":
            try:
                spotify_windows = gw.getWindowsWithTitle("Spotify Free")
                
                subprocess.Popen(['spotify'])
                # print(spotify_windows)
                # if spotify_windows:
                #     # If Spotify window exists, bring it to the foreground
                #     spotify_windows[0].activate()
                #     print("Spotify window is already open. Focused on Spotify.")
                # else:
                #     # If Spotify window doesn't exist, open Spotify application
                #     print("Spotify app is not running. Opened Spotify.")
                
                time.sleep(.1)
                if is_icon_present('lib\playIcon.png'):
                    # print('first')
                    pass
                else:
                    # print('second')
                    # pass
                    pag.press('space')
            except Exception as e:
                pass
        
        elif answer == 'next song':
            try:
                spotify_windows = gw.getWindowsWithTitle("Spotify Free")
                
                if spotify_windows:
                    # If Spotify window exists, bring it to the foreground
                    spotify_windows[0].activate()
                    print("Spotify window is already open. Focused on Spotify.")
                else:
                    # If Spotify window doesn't exist, open Spotify application
                    subprocess.Popen(['spotify'])
                    print("Spotify app is not running. Opened Spotify.")
                
                time.sleep(.1)
                if is_icon_present('lib\playIcon.png'):
                    pass
                else:
                    # pass
                    pag.press('space')
            except Exception as e:
                pass
        
        elif answer == 'exit spotify':
            print('exiting...')
            change_value_of_specified('spotify_control','no')
            return('exiting from spotify mod!!')
        
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.on_login_clicked)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Here you can implement your login logic
        # For simplicity, let's just print the username and password
        print("Username:", username)
        print("Password:", password)

        # Close the dialog
        self.accept()
