import string 
import random

def generar_contreseña (longitutd):
    caracteres=string.ascii_letters + string.digits + string.punctuation
    contrasena= ""
    for i in range (longitutd):
        contrasena += random.choice(caracteres)
    return contrasena 

longitud=int(input ("cual es el tamaño de la contraseña deseada: "))

nueva_contrasena= generar_contreseña(longitud)
nueva_contrasena= nueva_contrasena.lstrip("!#$%&/=?¡¡&/~,")
print("La nueva contraseña es: ",nueva_contrasena)