with open('task-1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите данные для добавления в текстовый файл: ')
        if not line:
            break
        print(line, file=f)