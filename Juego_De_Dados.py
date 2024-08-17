from tkinter import *
import random

Juego=Tk()
Juego.geometry("700x450")
Juego.title("Juego de Dados")

label=Label(Juego,text="",font=("time",260))

def girar():
    cantidad=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text=f"{random.choice(cantidad)}{random.choice(cantidad)}")
    label.pack()

boton=Button(Juego,text="LANZA LOS DADOS....",width=40,height=5,font=10,bg="white",
             bd=2,command=girar)
boton.pack(padx=10,pady=10)

Juego.mainloop()