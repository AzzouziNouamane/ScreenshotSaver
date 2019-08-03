import speech_recognition as sr


def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            return format(text)
        except:
            print("Sorry could not recognize what you said, retry :)")
