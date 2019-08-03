from pynput.keyboard import Key, KeyCode, Listener
import pyscreenshot as ImageGrab
import datetime
import speechRecognitionTester as speechRecognitionTester
import time
import pyautogui

# Your functions

def take_screenshot():
    print('Executing...')
    #if __name__ == '__main__':
    x = 1
    while x < 4 :
        pyautogui.screenshot('image'+str(x)+'.png')
        x += 1
        time.sleep(2)
#-#

def test_hotkey():
    with open("D:\logtext.txt", 'a') as File:
        File.write(str(datetime.datetime.now()) + '\n')

while (True):
    speech = speechRecognitionTester.speech_recognition()
    if speech is None:
        continue
    print (speech) 
    if('1' in speech):
        print('Gotta take a screen nigga')
        take_screenshot()
        #time.sleep(10)
        
    if('stop' in speech):
        break


exit()