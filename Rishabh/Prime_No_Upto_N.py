def isPrime(num):
    """Checks num for primality. Returns bool."""

    if num == 2:
        return True
    elif num < 2 or not num % 2:	# even numbers > 2 not prime
        return False

		# factor can be no larger than the square root of num
    for i in range(3, int(num ** .5 + 1), 2):
        if not num % i: return False
    return True



def generatePrimes(n):

    primes = [2,]
    noOfPrimes = 1
    testNum = 3
    while noOfPrimes < n:
        if isPrime(testNum):
            primes.append(testNum)
            noOfPrimes += 1
        testNum += 2

    return primes

#Make Driver Code
