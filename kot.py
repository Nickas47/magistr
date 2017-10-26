# -*- coding: utf-8 -*-

from tkinter import *
import time

root = Tk()
root.title("Program")
root['background'] ='gray'

def command_Print():
    for i in range(0, 10, 1):
        time.sleep(1)
        Label0.after(1)
        Labelvar.set(i)

Labelvar = StringVar()
Labelvar.set(u'original value')
Frame0 = Frame(root)
Frame0.place(x=0, y=0, width=100, height=50)
Label0 = Label(Frame0, textvariable=Labelvar, anchor='w')
Label0.pack(side=LEFT)


Frame_I = Frame(root)
Frame_I.place(x = 100, y = 0, width=100, height=70)
Button_I = Button(Frame_I, text = "Button" , width = 100, height=70, command = command_Print)
Button_I.place(x=0, y=0)
Button_I.grid(row=0, column=0, sticky=W, pady=4)
Button_I.pack()

root.mainloop()