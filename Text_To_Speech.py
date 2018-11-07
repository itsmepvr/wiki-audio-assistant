
#Text_To_Speech Code
#v_1.0
#Author : Venkata Ramana. P

import pyttsx
    
def speak(text):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voice')
    engine.setProperty('voice', voices[1])
    engine.setProperty('rate', 300)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()  
