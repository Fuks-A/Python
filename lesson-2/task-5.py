print("Пятая задача домашнего задания")
print()

a = [10, 5, 5, 2, 1, 5, 6, 4, 3, 3]
b = int(input("введите новое значение для добавления в список - "))
c = 0

for n in a:
    if b <= n:
        c += 1
a.insert(c, float(b))

print(a)