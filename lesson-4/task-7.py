def a(number):
    b = 1
    if number == 0:
        yield f"{number}! = 1"
    for i in range(1, number + 1):
        b *= i
        yield f"{i}! = {b}"
for el in a(int(input("вычисление факториала числа: "))):
    print(el)