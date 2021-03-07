def primesBelow(n):
    nums = [True] * n
    primes = []

    for i in range(2, n):
        if nums[i]:
            primes.append(i)
            nums[i*i::i] = [False] * len(nums[i*i::i])
    
    return primes


print(sum(primesBelow(int(2e6))))