primes = []
number = 1
while len(primes) < 10001:
    number += 1
    isPrime = True
    for i in primes:
        if not number % i:
            isPrime = False
            break

    if isPrime:
        primes.append(number)
        print(len(primes), number)
