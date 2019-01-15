import time
num = int(input('Dame un número'))
for i in range(num):
    print(num)
    num = num - 1
    time.sleep(1)
