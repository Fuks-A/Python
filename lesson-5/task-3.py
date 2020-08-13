with open('task-3.txt', "r", encoding="utf-8") as a:
    b = []
    c = []
    d = a.read().split('\n')
    for i in d:
        i = i.split()
        if float(i[1]) < 20000:
            c.append(i[0])
        b.append(i[1])
print(f'Зарпалата менее 20 000 {c}. Средняя зарплата – {sum(map(float, b)) / len(b)}')