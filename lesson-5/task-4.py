a = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task-4.txt', 'a', encoding='utf-8') as c:
    with open('task-4.txt', encoding='utf-8') as b:
        line = b.read().split("\n")
        for i in line:
            i = i.split(" - ")
            c.writelines(a[i[0]] + " - " + i[1] + "\n")