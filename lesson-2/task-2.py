print("Вторая задача домашнего задания")
print()

a = input("введите цифры без пробела - ").split()

for i in range(1, len(a), 1): a[i - 1], a[i] = a[i], a[i - 1]
print(a)