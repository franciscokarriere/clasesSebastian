import tkinter as tk
import random
from Point import Point


# clase ChaosGame numero de puntos para plotear 50000 por default, 
# canvas de 600 x 520

#Clase del juego
class ChaosGame:
    def  __init__(self,master, width=600, height=520, num_points=50000):
        self.master = master
        self.height=height
        self.width=width
        self.num_points=num_points

        #Definicion global de listas vacias para los vertices y midpoints
        self.vertices = []
        self.midpoints = []

        #configuracion de canva
        self.canvas=tk.Canvas(master, width=width, height=height)
        self.canvas.pack()
        self.canvas.config(bg="white")

        self.master.title("The Chaos Game!")


        #Llamado a funciones
        self.generate_vertices()
        self.plot_vertices()
        self.generate_midpoints()
    
    #Funcion para generar vertices
    # v1, v2, v3 ← three vertices of an equilateral triangle
    def generate_vertices(self):
        self.vertices.append(Point(100,400))
        self.vertices.append(Point(300,100))
        self.vertices.append(Point(500,400))
        
    def plot_vertices(self):
        