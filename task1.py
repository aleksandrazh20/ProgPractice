def season(m):
    if m == 1 or m == 2 or m == 12:
        return 'Зима'
    elif m == 3 or m == 4 or m == 5:
        return 'Весна'
    elif m == 6 or m == 7 or m == 8:
        return 'Лето'
    elif m == 9 or m == 10 or m == 11:
        return 'Осень'
    else:
        return 'Ошибка'

m = int(input())
print(season(m))