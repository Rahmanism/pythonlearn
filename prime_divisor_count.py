
def IsPrime(n):
    """
        Checks if the given number is prime
    """
    if n >= 2:
        half = n // 2 + 1
        for m in range(2,half):
            if not (n % m):
                return False
    else:
        return False
    return True

#-------------------------------------------

mainNumbers = list()
primeCount = dict()

# get numbers
for i in range(10):
    mainNumbers.append(int(input()))

# calculate divisors
for n in mainNumbers:
    primeDivisorsCount = 0
    half = n // 2 + 1
    for j in range(2, half):
        if n % j == 0:
            if IsPrime(j):
                primeDivisorsCount += 1
    primeCount[n] = primeDivisorsCount

max = mainNumbers[0]
for i in mainNumbers:
    if primeCount[i] > primeCount[max] \
        and i > max:
        max = i


print(max, primeCount[max])
