def isPrime(n):
    if n<1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True

def primeNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPrime(i):
            print(i)

primeNumbers(1,100)

