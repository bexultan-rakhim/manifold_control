import numpy as np
from matplotlib import pyplot as plt
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


def exponential_map(theta, N):
    
    def elements(theta, N):
    
        def even_odd(x, n):
            if n % 2 ==0:
                return np.array([x,0])
            else:
                return np.array([0,x])
    
        x = [even_odd(
                ((-1)**(i//2))*(theta**i)/np.math.factorial(i),
                i
                ) for i in range(N)
        ]
    
        return np.array(x)

    def vect(x, n):
        return np.sum(x[:n,:], 0)

    x = elements(theta, N)
    y = [vect(x,i) for i in range(0,N)]

    return np.array(y)

def circle(N):
    
    x = [np.array(
                [np.sin(2*np.pi*i/N),
                np.cos(2*np.pi*i/N)]
            ) for i in range(N+1)
        ]
    
    return np.array(x)

root = Tk()
root.title("Exponential Map")
root.geometry("400x400")


fig = Figure(figsize=(10,10), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
sbplt = fig.add_subplot(111)
sbplt.axis("square")
sbplt.grid("on")
sbplt.set_xlim([-2, 2])
sbplt.set_ylim([-2, 2])

def slide(var):
    circle_vals = circle(100)
    x = exponential_map(float(var), 100)
    sbplt.clear()
    sbplt.plot(circle_vals[:,0], circle_vals[:,1], 'r')
    sbplt.plot(x[:,0], x[:,1],'b')

    sbplt.axis("square")
    sbplt.grid("on")
    sbplt.set_xlim([-2, 2])
    sbplt.set_ylim([-2, 2])
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

slider = Scale(root, from_=-7, to= 7,resolution=0.1,length=300, orient=HORIZONTAL, command=slide)
slider.pack()


def _quit():
    root.quit()     
    root.destroy()

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)
root.mainloop()