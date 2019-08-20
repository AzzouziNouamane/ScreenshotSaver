from pynput.keyboard import Key, KeyCode, Listener
import pyscreenshot as ImageGrab
import datetime
import speechRecognitionTester as speechRecognitionTester
import time
import pyautogui
import pytesseract
from pynput import keyboard
from PIL import Image

x = 0

# Currently pressed keys
current_keys = set()
possible_keys = [Key.shift, KeyCode(char='a'), KeyCode(char='A'), KeyCode(char='v'), KeyCode(char='V'), KeyCode(char='b'), KeyCode(char='B')]

def on_press(key):
    print("On Press : ")
    print(key)
    print(current_keys)
    if (key in possible_keys):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
        current_keys.add(key)
        if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
            combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    print("On Release : ")
    print(key)
    print(current_keys)
    current_keys.remove(key)
    print(current_keys)


def take_screenshot():
    global x
    print('Executing...')
    #if __name__ == '__main__':
    pyautogui.screenshot('image' + str(x) + '.png')
    myScreenshot = Image.open('image' + str(x) + '.png')
    text = pytesseract.image_to_string(myScreenshot, lang='eng')
    print('My text is : ')
    print(text)
    x += 1
    print('Done')
    if Key.shift in current_keys:
        on_release(Key.shift)
    if KeyCode(char='a') in current_keys:
        on_release(KeyCode(char='a'))
    if KeyCode(char='A') in current_keys:
        on_release(KeyCode(char='A'))

def activate_voiceRecognition():
    print('Voice Recognition ON.')
    while(True):
        speech = speechRecognitionTester.speech_recognition()
        print (speech) 
        if speech is None:
            continue
        if('1' in speech):
            print('Gotta take a screen nigga')
            take_screenshot()
                #time.sleep(10)
                
        if('stop' in speech):
            break
    print('Voice Recognition OFF.')
    if Key.shift in current_keys:
        on_release(Key.shift)
    if KeyCode(char='v') in current_keys:
        on_release(KeyCode(char='v'))
    if KeyCode(char='V') in current_keys:
        on_release(KeyCode(char='V'))

def function_1():
    print('Executed function_1')

def function_2():
    print('Executed function_2')

# The key combination to check
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='a')]): take_screenshot, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.shift, KeyCode(char='A')]): take_screenshot,
    frozenset([Key.shift, KeyCode(char='V')]): activate_voiceRecognition,
    frozenset([Key.shift, KeyCode(char='v')]): activate_voiceRecognition,
    frozenset([Key.shift, KeyCode(char='b')]): exit,
    frozenset([Key.shift, KeyCode(char='B')]): exit,
}

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
with Listener(on_press=on_press, on_release=None) as listener:
    listener.join()