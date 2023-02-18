from random import random
n = int(input('Введите количество чисел в последовательности: '))
m = int(input('Введите верхнюю границу: '))
a = [0] * n
for i in range(n):
    a[i] = int(random() * m)
print(a)
setarr = set(a)
if len(a) == len(setarr):
    print('Нет дубликатов')
else:
    print('Есть дубликаты')