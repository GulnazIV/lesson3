n = int(input('Введите неотрицательное число\n'))
while n < 0:
    n = int(input('Введите неотрицательное число!!\n'))
temp, i = n, 0

while temp != 0:
    if n % temp == 0:
        i += 1
    temp -= 1

print('') if n in (0, 1) else print('Простое') if i == 2 else print('Составное')

