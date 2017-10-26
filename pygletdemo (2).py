from tkinter import *
 
def go():
        x,y=1,1
        c.move(krug,x,y)
        c.after(30,go)  #повторный вызов метода через 30 милесикунд
 
root=Tk()
c=Canvas(root,width=400,height=400,bg='#A6BDDC')
c.pack()
 
krug=c.create_oval(60,60,120,120,fill='#FFF70F',width=0)
 
go()
root.mainloop()