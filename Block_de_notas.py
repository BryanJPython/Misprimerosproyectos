from tkinter import *
import tkinter as tk
from tkinter import filedialog 

def nuevo_archivo():
    area_para_escribir.delete(1.0,tk.END)
    pass
def abrir_archivo():
    global nombre_archivo
    nombre_archivo=filedialog.askopenfilename(defaultextension=".txt", filetypes={("Archivos de textos ", "*.txt"),
                                                                             ("Archivos de python ", "*.py"),
                                                                            ("Todos los Archivos ", "*.*")})
    area_para_escribir.delete(1.0,tk.END)
    with open(nombre_archivo, "r", encoding="utf*8") as file:
        area_para_escribir.insert(tk.INSERT, file.read())
pass
def guardar_archivo():
        global nombre_archivo
        if nombre_archivo:
            try:
             with open (nombre_archivo, "w",encoding="utf*8") as file:
                file.write(area_para_escribir.get(1.0,tk.END))
            except:
                print("No se puede guardar el archivo ")
            
    
def guardar_archivo_como():
    nueva_ruta=filedialog.asksaveasfilename(defaultextension=".txt", filetypes={("Archivos de textos ", "*.txt"),
                                                                             ("Archivos de python ", "*.py"),
                                                                            ("Todos los Archivos ", "*.*")})
    if nueva_ruta:
        with open (nueva_ruta, "n") as file:
            file.write(area_para_escribir.get(1.0,tk.END))
            
    print(nueva_ruta)
    
    def copiar ():
        area_para_escribir.event_generate(("<<copy>>"))
    def pegar ():
        area_para_escribir.event_generate(("<<paster>>"))
    def cortar ():
        area_para_escribir.event_generate(("<<copy>>"))
        
ventana= tk.Tk()
ventana.title("Block de notas ")
ventana.geometry("800x600")
nombre_archivo=""


menu=tk.Menu(ventana)
ventana.config(menu=menu)

archivos=tk.Menu(menu)
menu.add_cascade(label="Archivos", menu=archivos)

edicion=tk.Menu(menu)
menu.add_cascade(label="Edicion", menu=edicion)

sobre_mi=tk.Menu(menu)
menu.add_cascade(label="Sobre Mi", menu=sobre_mi)

area_para_escribir=tk.Text(ventana)
area_para_escribir.pack(fill=tk.BOTH, expand=True)

archivos.add_command(label="Nuevo ", command= nuevo_archivo)
archivos.add_command(label="Abrir ", command= abrir_archivo)
archivos.add_command(label="Guardar ", command= guardar_archivo)
archivos.add_command(label="Guardar como  ", command= guardar_archivo_como)


ventana.mainloop()