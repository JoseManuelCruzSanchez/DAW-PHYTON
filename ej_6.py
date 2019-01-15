billete_50 = 0
billete_20 = 0
billete_10 = 0
billete_5 = 0
moneda_2 = 0
moneda_1 = 0

num = int(input('Dame una cantidad en euros: '))
while num > 0:
    if num >= 50:
        billete_50 = billete_50 + 1
        num = num - 50
    elif num >= 20:
        billete_20 = billete_20 + 1
        num = num - 20
    elif num >= 10:
        billete_10 = billete_10 + 1
        num = num - 10
    elif num >= 5:
        billete_5 = billete_5 + 1
        num = num - 5
    elif num >= 2:
        moneda_2 = moneda_2 + 1
        num = num - 2
    elif num >= 1:
        moneda_1 = moneda_1 + 1
        num = num - 1
        
print("Billetes de 50: " + str(billete_50))
print("Billetes de 20: " + str(billete_20))
print("Billetes de 10: " + str(billete_10))
print("Billetes de 5: " + str(billete_5))
print("Monedas de 2: " + str(moneda_2))
print("Monedas de 1: " + str(moneda_1))
