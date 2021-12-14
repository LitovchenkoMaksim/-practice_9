import time
from random import randint

start_time = time.time()
a = []
for i in range(100):
    a.append(randint(1, 100))

a.sort()
print(a)

value = int(input("введите искоме значение: "))


def find_id(list, value):
    mid = len(list) // 2
    low = 0
    high = len(list) - 1

    if len(list) <= 1:
        return "No value"

    if value == list[mid]:
        return value

    if value > list[mid]:
        del list[low:mid+1]
        return find_id(list, value)
    else:
        del list[mid - 1: high]
        return find_id(list, value)


print(find_id(a, value))
if value in a:
    print("ID =", a.index(value))
print("--- %s start_time = time.time()seconds ---" % (time.time() - start_time))
