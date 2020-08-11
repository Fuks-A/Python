print("Первая задача домашнего задания")
print()
a = [1, 0.25, 3 + 3j, "привет", 2.45, (7, 4), {"ц": 1, 'ф':3}, 111]
for i in range(len(a)):
    if type(a[i]) == dict:
        break
    print(a[i])