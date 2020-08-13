from itertools import count, cycle
print("Программа генерирует целые числа, начиная с указанного.")
for i in count(int(input("Введите первое число: "))):
    print(i, end =' ')
    quit = input()
    if quit == 'q':
        break
print('Программа повторяет элементы списка. Для генерации следующего повторения необходимо нажать Enter'
      'для выхода из программы – "q"')
a = input('Введите список, разделяя элементы пробелом: ').split()
iter = cycle(a)
quit = None
while quit != 'q':
    print(next(iter), end= '')
    quit = input()