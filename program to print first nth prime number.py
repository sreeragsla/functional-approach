def isPrime(n):
    if n<1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True

def firstnPrimeNumbers(count):
    c=0
    n=2
    while True:
        if isPrime(n):
            print(n)
            c+=1
            if c==count:
                break
        n+=1

firstnPrimeNumbers(10)


