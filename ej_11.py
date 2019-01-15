#Realizar el juego del ahorcado. La aplicación dispondrá de un diccionario de 25 palabras.
#Cuando se inicie el juego elegirá una de manera aleatoria. El usuario deberá de introducir
#letras para adivinar la palabra escondida. Solo se permitirán 6 fallos.

import random
class Ahorcado:
    palabras = []
    palabra = list()
    espacios_en_blanco = list()
    intentos = 6
    def __init__(self):
        f = open("ahorcado.txt")
        while True:
            linea = f.readline()
            if not linea:
                break
            self.palabras.append(linea[:-1])#linea[:-1] es un substring para elminar "\n"
        self.palabra = self.palabras[random.randrange(0, len(self.palabras))]

    def inicializar_espacios_en_blanco(self):
        for i in range(len(self.palabra)):
            self.espacios_en_blanco.append("_")
        print("La palabra buscada contiene " + str(len(self.palabra)) + " letras: " + self.palabra)
        print(''.join(self.espacios_en_blanco))



    def comprobar_letra(self, letra):
        if self.palabra.find(letra.upper()) != -1:
            for i in range(len(self.palabra)):
                if self.palabra[i] == letra.upper():
                    self.espacios_en_blanco.pop(i)
                    self.espacios_en_blanco.insert(i, letra.upper())
        else:
            self.intentos = self.intentos -1
            print("Error: Te quedan " + str(self.intentos) + " intentos.")
        print()
        print(''.join(self.espacios_en_blanco))

    def comprobar_palabras(self):
        return ''.join(x.palabra) == ''.join(x.espacios_en_blanco)

x = Ahorcado()
x.inicializar_espacios_en_blanco()

while True:
    if x.intentos > 0:
        letra = input("Introduce 1 nueva letra: ")
        x.comprobar_letra(letra)
        if x.comprobar_palabras():
            print("***************  FIN  *******************")
            print("*                                       *")
            print("*       FELICIDADES - HAS GANADO        *")
            print("*                                       *")
            print("***************  FIN  *******************")
            break
    else:
        print("***************  FIN  *******************")
        print("*                                       *")
        print("   Has consumido todos los intentos!!    ")
        print("   La palabra era: " + ''.join(x.palabra))
        print("*                                       *")
        print("***************  FIN  *******************")
        break

