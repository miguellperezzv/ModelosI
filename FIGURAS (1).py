# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:49:05 2019

@author: estudiantes
"""

#import tkinter
"""from tkinter import *



class Aplicacion():
    def __init__(self):
        frame = Tk()
        
        frame.geometry('700x700')
        frame.title('Figuras')
        frame.mainloop()
        canvas = Canvas(frame, width= 500, height=500)
        canvas.pack()
        canvas.create_rectangle(50, 20, 150, 80, fill="#476042")
    def key(event):
        print ("pressed", repr(event.char))

    def callback(event):
        print ("clicked at", event.x, event.y)                           
        canvas.bind("<Button-1>", callback)
        
        
        
def main():
    ventana = Aplicacion()
    def key(event):
        print ("pressed", repr(event.char))

    def callback(event):
        print ("clicked at", event.x, event.y)                           
        canvas.bind("<Button-1>", callback)



if __name__ == '__main__':
    main()
"""


from tkinter import *
import abc 
from abc import ABC
from numpy import array

class Figura(ABC):
    x=array ([0,0])
    y=array ([0,0])
    def __init__(self):
        __metaclass__=ABCMeta #metaclase
    abc.abstractmethod
    def dibujar(x, y):
        print(x)
        print(y)
        
class circulo(Figura):
    def __init__(self):
        pass
    def dibujar(x,y):
        print(x)
        print(y)

class Aplicacion():
    
    frame = Tk()
    clic=0
    xArr=array([0,0])
    yArr=array([0,0])
    
    def key(event):
        print ("pressed", repr(event.char))
    
    def listener(event):
        clic=clic+1
        print ("clickedaaaaa at+ clic", event.x, event.y, clic)
        if(clic==1):
            print("click ", clic)
            xArr[0]=event.x
            xArr[1]=event.y
        elif(clic==2):
            yArr[0]=event.x
            yArr[1]=event.y
            circulo =circulo(xArr,yArr)
            circulo.dibujar
        
    
    canvas= Canvas(frame, width=500, height=500)
    canvas.bind("<Key>", key)
    canvas.bind("<Button-1>", callback)
    canvas.pack()
    canvas.create_rectangle(50, 20, 350, 350, fill="#ffffff")
    frame.mainloop()
    


def main():
    ventana = Aplicacion()
    
if __name__ == '__main__':
    main()