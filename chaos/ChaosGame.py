import tkinter as tk
import random
from Point import Point


# clase ChaosGame numero de puntos para plotear 50000 por default, 
# canvas de 600 x 520
# 
class ChaosGame:
    def  __init__(self,master, width=600, height=520, num_points=50000):
        self.master = master
        self.height=height
        self.width=width
        self.num_points=num_points
        self.canvas=tk.Canvas(master,width=width,height=height)
        self.canvas.pack()

        self.master.title("The Chaos Game!")