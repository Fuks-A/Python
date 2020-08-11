print("Четвертая задача домашнего задания")
print()
num_int = int(input("Введите целое положительное число: "))
c = 0
num = num_int
while num > 0:
    e = num % 10
    if e > c:
        c = e
        if c == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_int} равна {c}")