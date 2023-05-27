import time

birthday = input('dd.mm.yyyy: ')
print(f"Вы прожили {int(time.time()-time.mktime(time.strptime(birthday,'%d.%m.%Y'))) // 86400} дней")