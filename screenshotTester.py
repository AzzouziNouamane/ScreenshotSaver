from pynput.keyboard import Key, KeyCode, Listener
import pyscreenshot as ImageGrab
import datetime

# Your functions

def take_screenshot():
    if __name__ == '__main__':
        print(ImageGrab.grab())
    # grab fullscreen
        im = ImageGrab.grab()

    # save image file
        im.save('screenshot.png')

    # show image in a window
        im.show()
#-#

def test_hotkey():
    with open("D:\logtext.txt", 'a') as File:
        File.write(str(datetime.datetime.now()) + '\n')

take_screenshot()
test_hotkey()