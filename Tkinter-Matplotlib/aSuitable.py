#coding:utf-8
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        #一定要加self否则tracker = IndexTracker(ax, X)无法调用
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()


def drawPic():
    fig, ax = plt.subplots(1, 1)
    X = np.random.rand(20, 20, 40)
    tracker = IndexTracker(ax, X)
    fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
    plt.show()
    # try:sampleCount=int(inputEntry.get())
    # except:
    #     sampleCount=50
    #     print '请输入整数'
    #     inputEntry.delete(0,END)
    #     inputEntry.insert(0,'50')

    #清空图像，以使得前后两次绘制的图像不会重叠
    # drawPic.f.clf()
    # drawPic.a=drawPic.f.add_subplot(111)

    #在[0,100]范围内随机生成sampleCount个数据点
    # x=np.random.randint(0,100,size=sampleCount)
    # y=np.random.randint(0,100,size=sampleCount)
    # color=['b','r','y','g']

    #绘制这些随机点的散点图，颜色随机选取
    # drawPic.a.scatter(x,y,s=3,color=color[np.random.randint(len(color))])
    # drawPic.a.set_title('Demo: Draw N Random Dot')
    # drawPic.canvas.show()


if __name__ == '__main__':

    matplotlib.use('TkAgg')
    root = Tk()
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
    drawPic.f = Figure(figsize=(8,6), dpi=100)

    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)

    Button(root,text='画图',command=drawPic).grid(row=1,column=2,columnspan=3)

    #启动事件循环
    root.mainloop()



