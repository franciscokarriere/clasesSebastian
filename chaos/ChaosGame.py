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
        self.plot_midpoints()
    
    #Funcion para generar vertices, se definen los puntos estaticos para el canva 600x520
    # v1, v2, v3 ← three vertices of an equilateral triangle
    def generate_vertices(self):
        self.vertices.append(Point(100,400))
        self.vertices.append(Point(300,100))
        self.vertices.append(Point(500,400))
        
    def plot_vertices(self):
        for vertex in self.vertices:
            self.canvas.create_oval(vertex.get_x() -3, vertex.get_y() - 3, vertex.get_x() +3, vertex.get_y() + 3, fill="blue")


# plot v1, v2, and v3
# p1, p2 ← two randomly selected vertices from v1, v2, and v3 m ← the midpoint of p1 and 
    def generate_midpoints(self):
        #Seleccion random de dos puntos p1, p2
        p1 = random.choice(self.vertices)
        p2 = random.choice(self.vertices)
        #m ← the midpoint of p1 and p2
        #Se calcula el punto medio de x e y
        mx = (p1.get_x() + p2.get_x())/2
        my = (p1.get_y() + p2.get_y())/2

        punto = Point(mx,my)
        self.midpoints.append(punto)
        
        while len(self.midpoints) < 1500:
            # v ← a randomly selected vertex from v1, v2, and v3
            v = random.choice(self.vertices)
            # m’ ← the midpoint of m and v
            m_prime_x = (self.midpoints[-1].get_x() + v.get_x())/2
            m_prime_y = (self.midpoints[-1].get_y() + v.get_y())/2
            self.midpoints.append(Point(m_prime_x, m_prime_y))

    def plot_midpoints(self):
        for midpoint in self.midpoints:
            self.canvas.create_oval(midpoint.get_x() - 1, midpoint.get_y() - 1, midpoint.get_x() + 1, midpoint.get_y() + 1, fill="black")

        


        


root = tk.Tk()
chaos_game = ChaosGame(root)
root.mainloop()
