# -*- coding: utf-8 -*-
import Tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

var=tk.StringVar()

l=tk.Label(window,bg='yellow',width=40,height=4,text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected '+var.get())

r1=tk.Radiobutton(window,text='Option A',variable=var,value='A',command=print_selection)
r1.pack()

r2=tk.Radiobutton(window,text='Option B',variable=var,value='B',command=print_selection)
r2.pack()

r2=tk.Radiobutton(window,text='Option C',variable=var,value='C',command=print_selection)
r2.pack()

window.mainloop()