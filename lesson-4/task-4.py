from random import randint
my_list = [randint(-10, 10) for i in range(20)]
print(f"source list \n {my_list} \n Norepetition list \n {my_list}")