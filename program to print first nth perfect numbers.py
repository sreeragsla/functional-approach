def isPerfect(n):
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if n==ds:
        return True
    else:
        return False

def firstnPerfectNumbers(count):
    n=1
    pc=0
    while True:
        if isPerfect(n):
            print(n)
            pc+=1
            if pc==count:
                break
        n+=1

firstnPerfectNumbers(4)

