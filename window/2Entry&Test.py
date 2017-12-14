# -*- coding: utf-8 -*-
import Tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x200')

#e=tk.Entry(window,show='*') 打出来的密码就都是*号
e=tk.Entry(window,show=None)
e.pack()

def insert_point():
    var=e.get()
    t.insert('insert',var) # insert有几种形式，在指针标出来的位置insert就是用的insert

def insert_end():
    var=e.get()
    t.insert('end',var)
    #t.insert(1.1,var) 在第1行第1列输入

b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()

b2=tk.Button(window,text='insert_end',command=insert_end)
b2.pack()
t=tk.Text(window,height=2)
t.pack()

window.mainloop()
