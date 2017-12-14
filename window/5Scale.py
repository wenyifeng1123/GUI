# -*- coding: utf-8 -*-
import Tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')



l=tk.Label(window,bg='yellow',height=1,text='empty')# width是以字符的宽度为基础
l.pack()

def print_selection(v):
    l.config(text='you have selected '+v)

# length是以pixel为基础,tickinterval是标签长度，resolution保留几位小数
s=tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,
           showvalue=0,tickinterval=3,resolution=0.01,command=print_selection)
s.pack()

window.mainloop()