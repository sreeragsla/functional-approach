def isPrime(n):
    if n<1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True

def reverse(n):
    rev=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        rev=rev*10+rem
    return rev

def isEmirpNumber(n):
    rev=reverse(n)
    if isPrime(n) and isPrime(rev)and rev!=n:
        return True
    else:
        return False

def printEmirpNumbers(n):
        if isEmirpNumber(n):
            print(n)

printEmirpNumbers(13)

    
