while True:
    num = int(input('Dame numero entre 20 y 50: '))
    if num >= 20 and num <= 50:
        result = 0
        for i in range(num+1):
            result = result + i
        print("Sumatorio: " + str(result))
        break