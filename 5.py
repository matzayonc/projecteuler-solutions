def lcm(a, b):
    for i in range(a, a*b+1):
        if not i % a and not i % b:
            return i


number = 1

for i in range(1, 21):
    number = lcm(number, i)
    print(i, number)