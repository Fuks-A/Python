mydict = {}
with open("task-6.txt", encoding="utf-8") as fobj:
    for line in fobj:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or (i >='0' and i <= '9')]).split()))
        mydict[name] = name_sum
print(f'{mydict}')