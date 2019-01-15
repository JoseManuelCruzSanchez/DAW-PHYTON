import sys
nums = []

suma = 0
multiplicacion = 1
valor_min = sys.maxsize
valor_max = -sys.maxsize

for i in range(5):
    nums.append(int(input('Dame un número: ')))
for num in nums:
    suma = suma + num
    multiplicacion = multiplicacion * num
    if num < valor_min:
        valor_min = num
    if num > valor_max:
        valor_max = num

media = suma / 5

print("suma: " + str(suma))
print("multiplicacion: " + str(multiplicacion))
print("minimo: " + str(valor_min))
print("maximo: " + str(valor_max))
print("media: " + str(media))

