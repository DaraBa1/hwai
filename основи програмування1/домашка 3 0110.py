import time

N = int(input("Введіть число N: "))

for i in range(N, 0, -1):
    print(i)
    time.sleep(1)  # Затримка в 1 секунду між числами

print("Старт!")