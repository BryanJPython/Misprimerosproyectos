import random

def obtener_palabra():
    # Puedes agregar más palabras a la lista
    palabras = ['python', 'programacion', 'ahorcado', 'desarrollador', 'algoritmo']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    estado = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return estado

def juego_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6
    letras_usadas = set()

    print("Bienvenido al juego del Ahorcado!")
    print("Tienes 6 intentos para adivinar la palabra.")

    while intentos_restantes > 0:
        estado_actual = mostrar_estado(palabra, letras_adivinadas)
        print("Palabra: ", estado_actual)
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")

        letra = input("Adivina una letra: ").lower()

        if letra in letras_usadas:
            print("Ya has usado esa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Correcto!")
        else:
            intentos_restantes -= 1
            print("Incorrecto!")

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra '{palabra}'")
            break
    else:
        print(f"Se acabaron los intentos. La palabra era '{palabra}'")

if __name__ == "__main__":
    juego_ahorcado()
