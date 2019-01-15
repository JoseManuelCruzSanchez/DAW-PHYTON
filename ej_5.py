cad1 = input('Dame cadena de igual longitud a la siguiente:')
cad2 = input('Dame cadena de igual longitud a la anterior:')
resultado = ""
for i in range(len(cad1)):
    resultado += cad1[i] + cad2[i]
print(resultado)