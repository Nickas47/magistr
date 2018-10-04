from math import*
from tkinter import*

def draw(event): # функція для малювання крапки
        canv.create_oval(event.x - brush_size,
                              event.y - brush_size,
                              event.x + brush_size,
                              event.y + brush_size, fill="gray50")


f='Arial 8'
#функція
w1=80
h1=40
w=100
h=40


a=ceil((w-w1)/20)
b=ceil((h-h1)/20)
n=factorial(a+b)/(factorial(b))/(factorial(a))

xm1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ym1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xm2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ym2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

w2=w1
h2=h1

i=0
while i<=a:        
        xm1[i]=w2
        ym1[i]=h1
        w2+=20
        i+=1

i=0
while i<=b:
        xm2[i]=w1
        ym2[i]=h2
        h2+=20
        i+=1
        


brush_size = 6
x1=w1
y1=h1

def go():
        global x1,y1,xm1,ym1,xm2,ym2,a,b,h1,w1
        i = 0
        while i <= a:
                if xm1[i] <= x1:
                        if ym1[i] <= h:
                                canv.create_oval(xm1[i],ym1[i],xm1[i],ym1[i], width=2,outline="black")
                        ym1[i] += 4
                i+=1

        x1 += 4
        canv.after(40,go)


def gov():
        global x1,y1,xm1,ym1,xm2,ym2,a,b,h1,w1
        i=0
        while i <= b:
                if ym2[i] <= y1:
                        if xm2[i] <= w:
                                canv.create_oval(xm2[i],ym2[i],xm2[i],ym2[i], width=2,outline="black")
                        xm2[i] += 4
                i+=1

        y1 += 4
         
        canv.after(40,gov)

root=Tk()
canv=Canvas(root, width=562,height=523, bg="#fff")
canv.pack()

canv.create_line(20, 0, 20, 526, width=3,arrow="both", fill="blue")
canv.create_line(0, 500, 413, 500, width=3,arrow="last", fill="blue")

y=20
while y<510:
        canv.create_line(0,y,410,y,fill="grey")
        y+=20
 
x=20
while x<410:
        canv.create_line(x,0,x,510,fill="grey")
        x+=20

x,y=12,6
z=('X')# абсциса
for t in z:
        canv.create_text(x,y,text=t,font=f)
x,y=8,20
z=('24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1')
for t in z:
        canv.create_text(x,y,text=t,font=f)
        y+=20
x,y=400,515
z=('Y') # ордината 
for t in z:
        canv.create_text(x,y,text=t,font=f)
x,y=10,510
z=('0')
for t in z:
        canv.create_text(x,y,text=t,font=f)
        x+=20
x,y=40,518
z=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18')
for t in z:
        canv.create_text(x,y,text=t,font=f)
        x+=20

y = 19
while y < 490:
    x=39
    while x < 410:
        canv.create_oval(x,y,x+2,y+2, width=4, outline="red")
        x=x+20
    y = y + 20


gov()
go()

canv.bind("<Button-1>", draw) # кнопка миші яка відповідає за крапку

but = Button(root,
          text="Розрахувати", 
          width=15,height=2, 
          bg="white",fg="blue") 
but.place(x = 430, y = 30) 

canv.create_text(500,200,text="Кількість ходів:")
canv.create_text(500,220,text=n)
#інпути для вводу значень
canv.create_text(455,90,text="x1:")
ent_x1 = Entry(root,width=3,bd=3)
canv.create_text(500,90,text="y1:")
ent_y1 = Entry(root,width=3,bd=3)
ent_x1.place(x=465,y=80)
ent_y1.place(x=510,y=80)

canv.create_text(455,110,text="x2:")
ent_x2 = Entry(root,width=3,bd=3)
canv.create_text(500,110,text="y2:")
ent_y2 = Entry(root,width=3,bd=3)
ent_x2.place(x=465,y=100)
ent_y2.place(x=510,y=100)
root.mainloop()
