# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import Image,ImageTk # tkinter自带的tk.PhotoImage只能打开gif,所以用Image开jpg图片

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas=tk.Canvas(window,bg='blue',height=100,width=200)
image_file = Image.open('E:/pycharm/workspace/TkinterLearn/Lasso.png')
im = ImageTk.PhotoImage(image_file)
'''
0,0是左上角的起始点，然后anchor代表把画布钉在的位置
NW      N       NE

W       CENTER  E

SW      S       SE
'''
image=canvas.create_image(10,10,anchor='nw',image=im)
x0, y0, x1, y1= 50, 50, 80, 80
line=canvas.create_line(x0, y0, x1, y1)
oval=canvas.create_oval(x0, y0, x1, y1,fill='red') #填色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)   #创建一个矩形
canvas.pack()

def moveit():
    canvas.move(rect,0,2)#x移动0，y移动2
b=tk.Button(window,text='move',command=moveit).pack()

window.mainloop()