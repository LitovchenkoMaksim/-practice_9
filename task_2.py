import time
from random import randint
start_time = time.time()
a = []
for i in range(100):
    a.append(randint(1, 100))

a.sort()
print(a)

mid = len(a)//2
low = 0
high = len(a) - 1

value = int(input("введите искоме значение: "))

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print(value)
    print("ID", mid)



print("--- %s start_time = time.time()seconds ---" % (time.time() - start_time))
