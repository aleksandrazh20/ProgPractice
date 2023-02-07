from random import random
n = int(input('Введите количество чисел в последовательности: '))
m = int(input('Введите верхнюю границу: '))
a = [0] * n
for i in range(n):
    a[i] = int(random() * m)
print(a)
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] == a[j]:
            print('Есть дубликаты')
            quit()
print('Нет дубликатов')