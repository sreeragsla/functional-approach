def isDisarium(n):
    while True:
        dummy=n
        summ=0
        p=len(str(n))
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**p
            p-=1
        if n==summ:
            return True
        else:
            return False

def firstnDisariumNumbers(count):
    dc=0
    n=1
    while True:
        if isDisarium(n):
            print(n)
            dc+=1
            if dc==count:
                break
        n+=1

firstnDisariumNumbers(15)
