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

def disariumNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isDisarium(i):
            print(i)

disariumNumbers(1,1000)

                
