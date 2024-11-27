def isPerfect(n):
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if n==ds:
        return True
    else:
        return False

def perfectNumber(n):
    if isPerfect(n):
        print(n)

perfectNumber(28)
