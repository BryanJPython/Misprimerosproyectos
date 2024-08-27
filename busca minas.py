import tkinter as tk
from tkinter import messagebox
import random

class BuscaminasApp:
    def __init__(self, master, tamano=8, num_minas=10):
        self.master = master
        self.tamano = tamano
        self.num_minas = num_minas
        self.tablero = [[' ' for _ in range(tamano)] for _ in range(tamano)]
        self.vista = [[' ' for _ in range(tamano)] for _ in range(tamano)]
        self.minas = set()
        self.juegos_perdidos = False
        self.cargar_minas()
        self.crear_interfaz()

    def cargar_minas(self):
        while len(self.minas) < self.num_minas:
            mina = (random.randint(0, self.tamano - 1), random.randint(0, self.tamano - 1))
            if mina not in self.minas:
                self.minas.add(mina)
                self.tablero[mina[0]][mina[1]] = '*'

    def contar_minas_alrededor(self, x, y):
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        contador = 0
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.tamano and 0 <= ny < self.tamano and self.tablero[nx][ny] == '*':
                contador += 1
        return contador

    def revelar_casilla(self, x, y):
        if self.vista[x][y] != ' ':
            return
        mina = self.tablero[x][y]
        if mina == '*':
            self.vista[x][y] = '*'
            self.juegos_perdidos = True
            self.mostrar_tablero()
            messagebox.showinfo("Fin del juego", "¡Oh no! Has pisado una mina. ¡Juego terminado!")
            return True
        minas_alrededor = self.contar_minas_alrededor(x, y)
        self.vista[x][y] = str(minas_alrededor) if minas_alrededor > 0 else ' '
        if minas_alrededor == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < self.tamano and 0 <= y + dy < self.tamano:
                        self.revelar_casilla(x + dx, y + dy)
        return False

    def crear_interfaz(self):
        self.botones = [[None for _ in range(self.tamano)] for _ in range(self.tamano)]
        for i in range(self.tamano):
            for j in range(self.tamano):
                boton = tk.Button(self.master, width=3, height=2, command=lambda x=i, y=j: self.pulsar_boton(x, y))
                boton.grid(row=i, column=j)
                self.botones[i][j] = boton
        self.mostrar_tablero()

    def pulsar_boton(self, x, y):
        if not self.juegos_perdidos:
            if self.revelar_casilla(x, y):
                return
            self.actualizar_botones()
            if not any(self.vista[x][y] == ' ' for x in range(self.tamano) for y in range(self.tamano) if (x, y) not in self.minas):
                self.mostrar_tablero()
                messagebox.showinfo("¡Felicidades!", "¡Has ganado!")
                
    def actualizar_botones(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                if self.vista[i][j] == '*':
                    self.botones[i][j].config(text='*', bg='red')
                elif self.vista[i][j] == ' ':
                    self.botones[i][j].config(text='', bg='lightgrey')
                else:
                    self.botones[i][j].config(text=self.vista[i][j], bg='lightgrey')
                    
    def mostrar_tablero(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                if (i, j) in self.minas:
                    self.botones[i][j].config(text='*', bg='red')
                elif self.vista[i][j] != ' ':
                    self.botones[i][j].config(text=self.vista[i][j], bg='lightgrey')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Buscaminas")
    app = BuscaminasApp(root, tamano=8, num_minas=10)
    root.mainloop()
