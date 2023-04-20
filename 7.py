def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


n = int(input('Введите число больше 0\n'))
while n <= 0:
    n = int(input('Введите число больше 0!!\n'))

print(fib(n))
