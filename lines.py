# Testing skills in game programming

from tkinter import *

root = Tk()
root.title("Python game testing")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
root.update()

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 100, 100)

        self.canvas_height = canvas.winfo_wigth()
        self.x = -1
        self.y = 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_height:
            self.x = -1

        self.canvas.after(5, self.draw)


ball = Ball(canvas, "red")
ball.draw()

root.mainloop()