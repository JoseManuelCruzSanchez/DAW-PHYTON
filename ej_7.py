cad = input('Dame frase sin puntos: ')
vocal = 0
consonante = 0
espacio = 0
for i in range(len(cad)):
    if cad[i] == 'a' or cad[i] == 'e' or cad[i] == 'i' or cad[i] == 'o' or cad[i] == 'u':
        vocal = vocal + 1
    elif cad[i] == " ":
        print(cad[i])
        espacio = espacio + 1
    else:

        consonante = consonante + 1

print("Vocales: " + str(vocal))
print("Consonantes: " + str(consonante))
print("Espacios: " + str(espacio))