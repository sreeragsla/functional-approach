def isPrime(n):
    if n<1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
def printPrime(N):
    if isPrime(N):
        print(N)

printPrime(3)

