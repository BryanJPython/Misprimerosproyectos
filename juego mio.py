from tkinter import *
import random

Juego=Tk()
Juego.geometry("800x600")
Juego.title("Juego de Cartas")

label=Label(Juego,text="", font=("Time",300))

carta_pica= "\u2660"
carta_trebol= "\u2663"
carta_corazon= "\u2665"
carta_espalda= "\u2666"

def mostar_carta():
     cantidad=[carta_pica,carta_trebol,carta_corazon,carta_espalda]
     label.configure(text=f"{random.choice(cantidad)}{random.choice(cantidad)}")
     label.pack()
    
boton=Button(Juego,text="ADIVINA LAS CARTAS....",width=40,height=5,font=10,bg="white",
             bd=2,command=mostar_carta)
boton.pack(padx=10,pady=10)



Juego.mainloop()