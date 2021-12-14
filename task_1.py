import time
from random import randint
start_time = time.time()
a = []
for i in range(100):
    a.append(randint(1, 100))

a.sort()
print(a)

i = 0
x = int(input("Введите искомое значение: "))
b = 0
while b == 0 and i != len(a):
    if a[i] == x:
        print(x)
        print("ID", a.index(x))
        b = 1
        break
    i += 1

if b == 0:
    print("No value")

print("--- %s start_time = time.time()seconds ---" % (time.time() - start_time))
