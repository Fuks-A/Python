counter = 0
with open('task-2.txt', 'r', encoding='utf-8') as a:
    for line in a:
        counter +=1
        line_words = line.split()
        print(line, 'Длина строки: ', len(line_words))
    print('всего строк: ', counter)