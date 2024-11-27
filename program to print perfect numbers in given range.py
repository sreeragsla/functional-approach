def isPerfect(n):
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if n==ds:
        return True
    else:
        return False

def perfectNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isPerfect(i):
            print(i)

perfectNumbers(1,1000)

