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

def disariumNumber(N):
    if isDisarium(N):
        print(N)

disariumNumber(135)
