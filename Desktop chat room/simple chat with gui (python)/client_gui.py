# -*- coding: utf-8 -*-
"""

"""
from tkinter import *
from tkinter import messagebox
from socket import *
import _thread
s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 9000
s.connect((host, port))
wind = Tk()
wind.title('client')
wind.geometry('1000x500')
wind.configure(background='#2e59d1')
# A StringVar is a special type of variable in Tkinter that can be used to store and manipulate string values.

entryText = StringVar()
# The textvariable option is used to link the contents of the Entry widget to the value of the StringVar variable
en = Entry(wind, width=100, textvariable=entryText)
en.grid(column=1, row=1)
btn = Button(wind, width=3, height=1, text="send")
btn.grid(column=1, row=2)
r = 3


def rec():
    global r, s, lab
    while True:
        w = s.recv(2048)
        # we use the received text and make it the text of the button
        Button(wind, text=w.decode('utf-8'), bd=5, relief=FLAT, bg='#d1c62e',
               padx=5, pady=5, wraplength=100).grid(column=0, row=r)
        r = r+1


# embty tuble means tha it takes no arguments
# and we must make it to make the rec function workin to show the recieved messages
# if it isnt there will be no communication between the two sides
_thread.start_new_thread(rec, ())
# thread takes two arguments (target fun,arguments of it)


def clicked():
    global r, s, lab, entryText
    s.send((en.get()).encode('utf-8'))
    x = en.get()
    Button(wind, text=x, bd=5, relief=FLAT, bg='#d12e44',
           padx=5, pady=5, wraplength=100).grid(column=2, row=r)
    entryText.set("")
    r = r+1


btn["command"] = clicked
wind.mainloop()
