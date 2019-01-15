#Escribir una clase Python que permita las siguientes funciones: (10 puntos)
#• Añadir un número a la lista
#• Vaciar la lista de números
#• Ordenar de menor a mayor
#• Ordenar de mayor a menor
#• Calcular la media de la lista de números
#• Calcular mediana de la lista de números
#• Obtener una lista de números de un fichero de texto

class Numeros:
    numeros = []
    def __init__(self):
        self.numeros = []

    def anadir_numero_lista(self, numero):
        self.numeros.append(numero)

    def vaciar_lista(self):
        numeros = []

    def ordenar_menor_mayor(self):
        for x in range(len(self.numeros)):
            for y in range(len(self.numeros)):
                if self.numeros[y] > self.numeros[x]:
                    aux = self.numeros[x]
                    self.numeros[x] = self.numeros[y]
                    self.numeros[y] = aux

    def ordenar_mayor_menor(self):
        for x in range(len(self.numeros)):
            for y in range(len(self.numeros)):
                if self.numeros[y] < self.numeros[x]:
                    aux = self.numeros[x]
                    self.numeros[x] = self.numeros[y]
                    self.numeros[y] = aux

    def media_lista_numeros(self):
        media = 0
        for num in self.numeros:
            media = media + num
        return media / len(self.numeros)

    def mediana_lista_numeros(self):
        self.ordenar_menor_mayor()
        if len(self.numeros) % 2 == 0:
            indice = int(len(self.numeros) / 2 - 1)
            return (self.numeros[indice] + self.numeros[indice + 1]) / 2
        else:
            indice = int(len(self.numeros) / 2)
            return self.numeros[indice]

    def leer_fichero_numeros(self):
        f = open("fichero.txt")
        while True:
            linea = f.readline()
            if not linea:
                break
            self.numeros.append(int(linea))
    def imprimir(self):
        for num in ob_numeros.numeros:
            print(num)

ob_numeros = Numeros()

ob_numeros.leer_fichero_numeros()
print("--- Lectura fichero")
ob_numeros.imprimir()
print("--- Mediana")
print(ob_numeros.mediana_lista_numeros())
print("--- Media")
print(ob_numeros.media_lista_numeros())
print("--- Mayor a menor")
ob_numeros.ordenar_mayor_menor()
ob_numeros.imprimir()
print("--- Menor a mayor")
ob_numeros.ordenar_menor_mayor()
ob_numeros.imprimir()
print("--- Añadir 89")
ob_numeros.anadir_numero_lista(89)
ob_numeros.imprimir()
print("--- Vaciar lista")
ob_numeros.vaciar_lista()
ob_numeros.imprimir()
print("---")