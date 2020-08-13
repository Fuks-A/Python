print("Четвертая задача домашнего задания")
print()

a = input("Введите слова через пробел - ").split()

for i, b in enumerate(a, 1):
    print(f'{i} {b[:10]}')