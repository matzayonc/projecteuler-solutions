def primes():
    prime = []
    number = 1
    while True:
        number += 1
        isPrime = True
        for i in prime:
            if not number % i:
                isPrime = False
                break

        if isPrime:
            prime.append(number)
            yield number

number = 600851475143 

while number != 1:
    for prime in primes():
        if number % prime:
            continue

        number /= prime
        print(prime)
