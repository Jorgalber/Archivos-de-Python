# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 16:03:02 2022

@author: Jorge
"""

from tkinter import*;
import pandas as pd;
import matplotlib.pyplot as plt;
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

padding=10;
raiz=Tk();
raiz.title("Prueba Graficos");

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    plt.plot(event.xdata, event.ydata, 'Pr')
    fig.canvas.draw()
    
fig=Figure(figsize=(5, 5))
ax=fig.add_subplot().plot;


canvas=FigureCanvasTkAgg(fig,master=raiz)
canvas.get_tk_widget().grid(row=1,column=1,columnspan=2,padx=padding,pady=padding);



canvas.draw()



fig.canvas.mpl_connect('button_press_event', onclick)

Label(raiz, text="N:").grid(row=2,column=1,padx=padding,pady=padding)
cuadro=Entry(raiz);
cuadro.grid(row=2,column=2,padx=padding,pady=padding);

boton=Button(raiz,text="Inicio", width=3);
boton.grid(row=3,column=1,columnspan=2);

raiz.mainloop();