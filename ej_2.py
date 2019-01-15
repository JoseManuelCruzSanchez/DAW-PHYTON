while True:
    num = int(input('Dame numero entre 1 y 9: '))
    if num >= 1 and num <= 9:
        for i in range(11):
            print(str(i) + " x " + str(num) + " = " + str(i*num))
        break