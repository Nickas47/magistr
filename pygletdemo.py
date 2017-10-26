from math import *
from tkinter import *

x1=0
x2=0
y1=2
y2=2
y3=2
def go():
        global x1,x2,y1,y2,y3
        id1=canv.create_oval(x1,y1,x1,y1, width=2,outline="green") # пряма по х
        id2=canv.create_oval(x1,y2,x1,y2, width=2,outline="green")
        id3=canv.create_oval(x2,y3,x2,y3, width=2,outline="green")
        canv.move(id1, 17, 17)
        canv.move(id2, 17.5, 17)
        canv.move(id3, 17.5, 17)
        x1+=3
        y1+=3
        y3+=3
        canv.after(40,go)

root=Tk()
root.title("Цілочисельна решітка")
root.geometry("600x540+300+300")
def new_win():
     win = Toplevel(root)

def close_win():
     root.destroy()


f='Arial 8'
w,h=410,510
brush_size = 6

canv=Canvas(root,width=609,height=825,bg='white')
canv.pack()


def draw(event): # функція для малювання крапки
        canv.create_oval(event.x - brush_size,
                              event.y - brush_size,
                              event.x + brush_size,
                              event.y + brush_size, fill="gray50")


 

y=20
while y<h:
        canv.create_line(0,y,w,y)
        y+=20
 
x=20
while x<w:
        canv.create_line(x,0,x,h)
        x+=20
y = 17.5
while y < h:
    x=17.5
    while x < w:
        canv.create_oval(x,y,x+5,y+5, fill="red")
        x=x+20
    y = y + 20

canv.create_line(20, 0, 20, 526, width=2,arrow="both", fill="blue")
canv.create_line(0, 500, 413, 500, width=2,arrow="last", fill="blue")

x,y=12,6
z=('X')# абсциса
for t in z:
        canv.create_text(x,y,text=t,font=f)
x,y=8,16
z=('24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1')
for t in z:
        canv.create_text(x,y,text=t,font=f)
        y+=20
x,y=400,515
z=('Y') # ордината 
for t in z:
        canv.create_text(x,y,text=t,font=f)
x,y=25,518
z=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18')
for t in z:
        canv.create_text(x,y,text=t,font=f)
        x+=20



go()

canv.place(x = 0, y = 0)

but = Button(root,
          text="Розрахувати ходи", 
          width=15,height=2, 
          bg="white",fg="blue") 
but.place(x = 430, y = 50) 


canv.bind("<Button-1>", draw) # кнопка миші яка відповідає за крапку

m = Menu(root) #створюємо Меню 
root.config(menu=m) 
fm = Menu(m) #создается пункт меню м меню (m)
m.add_cascade(label="File",menu=fm) 
fm.add_command(label="New",command=new_win)
fm.add_command(label="Exit",command=close_win)

root.mainloop()