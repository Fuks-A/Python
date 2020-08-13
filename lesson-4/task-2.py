a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b=[a[num] for num in range(1, len(a)) if a[num] > a[num-1]]
print(b)