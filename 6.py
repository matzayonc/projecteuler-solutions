squareOfSum = 0
sumOfSquares = 0

for i in range(1, 101):
    sumOfSquares += i*i
    squareOfSum += i

print(squareOfSum**2 - sumOfSquares)
