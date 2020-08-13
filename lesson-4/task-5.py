from functools import reduce
def a (b, c):
    return b * c
d = [el for el in range(100,1001)]
print(f"список \n {d} \n результат умножение чисел \n {reduce(a, d)}")