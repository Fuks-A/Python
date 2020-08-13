from sys import argv
def salary():
    try:
        time, stavka, premia = map(float, argv[1:])
        print(f"Зарплата – {time * stavka + premia}")
    except ValueError:
        print("Введите значения выробатки в часах, ставка в час и сумму премии.")
salary()
