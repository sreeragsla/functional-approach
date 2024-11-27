def isArmstrong(n):
    while True:
        dummy=n
        summ=0
        p=len(str(n))
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem**p
        if n==summ:
            return True
        else:
            return False
def armstrongNumber(N):
    if isArmstrong(N):
        print(N)

armstrongNumber(153)
