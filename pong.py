#!/usr/bin/env python3
 
from tkinter import *
 
class Window:
    squads = []
    def __init__(self, master=None):
        self.can = Canvas(master, width = 500, height = 500,bg = 'grey80')
        self.can.pack()
        
        self.side = side = 50
        tup = tuple((x, y) for y in (i * side for i in range(10)) \
                           for x in (i * side for i in range(10)))
        self.tup = tup
        for x1, y1 in tup:
            x2, y2 = x1 + side, y1 + side
            self.squads.append(self.can.create_rectangle(x1, y1, x2, y2, width=3))
        for x in self.squads:
            self.can.tag_bind(x, "<Any-Enter>", self.mouseEnter)
            self.can.tag_bind(x, "<Any-Leave>", self.mouseLeave)
    
    def mouseEnter(self, event):
         self.can.itemconfig(CURRENT, fill = "red")
         for i, t in enumerate(self.tup, 1):
             x, y = t
             if x < event.x < x + self.side - 1 and \
                y < event.y < y + self.side - 1:
                    print(i)
                    break
    
    def mouseLeave(self, event):
        self.can.itemconfig(CURRENT, fill="grey80")
 
win = Tk()
obj = Window(win)
win.mainloop()