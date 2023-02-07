def count_summ(n):
    summ = 0
    while n > 0:
        digit = n % 10
        summ = summ + digit
        n = n // 10
    return summ

n = int(input())
print(count_summ(n))