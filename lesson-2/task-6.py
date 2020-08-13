print("Шестая задача домашнего задания")
print()
a = []
b = {"наименование": "", "цена": "", "количество": "", "единица измерения": ""}
c = {"наименование": [], "цена": [], "количество": [], "единица измерения": []}
d = 0
while True:
    for f in b.keys():
        e = input(f'введите "{f}" товара: ')
        b[f] = int(e) if (f == 'цена' or f == 'количество') else e
        c[f].append(b[f])
    a.append((d, b))
    print()
    print(f'текущая аналитика : ')
    for key, value in c.items():
        print(f'{key}: {value}')
    print()