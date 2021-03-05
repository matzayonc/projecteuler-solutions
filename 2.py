even = 0
a, b = 1, 0

while a < 4e6:
    a, b = a+b, a
    if not a % 2:
        even += a

print(even)