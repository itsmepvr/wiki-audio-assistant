
#Creating main gui using tkinter
#v_1.0
#Author : Venkata Ramana. P

from Tkinter import *
import sqlite3
import time
import datetime
import tkMessageBox
import requests
from Text_To_Speech import speak
from Browse_News import browse_wikipedia, browse_news
from idlelib.ToolTip import *


def Wiki_Speak():
    input2 = input1.get()
    if input2 is "":
        error = "error"
    else:
        output = browse_wikipedia(input2)
        print(output)
        speak(output)
        
def Tech_News():
    output = browse_news()
    print(output)
    speak(output)

def Stop_Voice():
    speak("")
    master.quit()
    
master = Tk()

master.overrideredirect(1)
w = 300 # width for the Tk root
h = 300 # height for the Tk root

# get screen width and height
ws = master.winfo_screenwidth() # width of the screen
hs = master.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2)  - (h/2)

# set the dimensions of the screen 
# and where it is placed
#master.geometry("300x300+100+100")
master.geometry('%dx%d+%d+%d' % (w, h, x, y))
master.attributes('-alpha', 0.9)
master.configure(background='black')

input1 = StringVar()        
label = Label(master, text = '', background = 'black')
label.pack()
input = Entry(master, insertbackground = 'white', textvariable = input1, bd=0, font = ('arial',12,'bold'), width = 20, background = 'black', foreground = 'white', justify = 'center')
input.focus()
input.pack()

WikiSpeak = Button(master, text = "Wiki Speak", command = Wiki_Speak, border = '0.5', background = 'black', foreground = 'white', font = ('arial',12,'bold'), activebackground = 'black', highlightcolor = 'black')
WikiSpeak.pack(side = TOP, pady = (20,0))

TechNews = Button(master, text = "Tech News", command = Tech_News, border = '0.5', background = 'black', foreground = 'white', font = ('arial',12,'bold'), activebackground = 'black', highlightcolor = 'black')
TechNews.pack(side = TOP, pady = (20,0))

Terminate = Button(master, text = "Terminate", command = Stop_Voice, border = '0.5', background = 'black', foreground = 'white', font = ('arial',12,'bold'), activebackground = 'black', highlightcolor = 'black')
Terminate.pack(side = TOP, pady = (20,0))

master.mainloop()

