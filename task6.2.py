import time
def prog(x):
    while x > 0:
        x -= 10

time1 = time.time()
x = 10000
prog(x)
time2 = time.time() - time1
file = time.strftime('%H.%M.%S %d.%m.%Y') + '.txt'
with open(file, 'w', encoding='utf-8') as f:
    f.write(str(time2))