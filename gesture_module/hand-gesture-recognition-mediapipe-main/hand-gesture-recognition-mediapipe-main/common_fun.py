import datetime
import pyttsx3
import webbrowser
import numpy as np
import cv2
import os
import re
import pyautogui as pag

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning, How may i help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, How may i help you?")
    else:
        speak("Good night, How may i help you?")

def is_number_present(text):
    # Regular expression to match any number in words
    pattern = r'(?:zero|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|Twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|thirtieth|fortieth|fiftieth|sixtieth|seventieth|eightieth|ninetieth|hundred|thousand|million|billion|trillion)'

    # Search for any number in words in the text
    match = re.search(pattern, text, flags=re.IGNORECASE)
    print(match)
    # Return True if a match is found, otherwise False
    return match is not None


def find_number(text):
    # Regular expression to match a number
    pattern = r'\d+'

    # Use re.findall() to find all occurrences of the pattern in the text
    numbers = re.findall(pattern, text)
    # Convert the list of strings to integers (if needed)
    numbers = [int(number) for number in numbers]

    return numbers

def open_drive(drive_letter):
    drive_letter = drive_letter.replace(' ','')
    drive_path = f"{drive_letter}:\\"
    print(drive_path)
    # Check if the drive exists
    if os.path.exists(drive_path.upper()):
        # Open the drive
        os.startfile(drive_path.upper())
        print(f"Drive {drive_letter.upper()} opened successfully.")
        return 'file opened'
    else:
        print(f"Drive {drive_letter} does not exist.")
        return 'file doesnt exits'
def search_link(url):
    # Initialize a new instance of the Chrome web driver
    webbrowser.open(url)

    
def is_icon_present(icon_image_path, threshold=0.9):
    # Capture screenshot
    screenshot = pag.screenshot()

    # Convert screenshot to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Load icon image as BGR
    icon_image = cv2.imread(icon_image_path)

    # Convert icon image to grayscale
    icon_gray = cv2.cvtColor(icon_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, icon_gray, cv2.TM_CCOEFF_NORMED)

    # Get the locations with similarity scores above the threshold
    loc = np.where(result >= threshold)

    # Check if any matches are found
    if loc[0].size > 0:
        return True
    else:
        return False

print(is_number_present('switch to second apples in the basket.'))