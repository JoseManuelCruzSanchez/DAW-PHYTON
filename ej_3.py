num = int(input('Dame numero: '))
resultado = 1
for i in range(num+1):
    if i != 0:
        print(i)
        resultado = resultado * i
print("Factorial: " + str(resultado))
