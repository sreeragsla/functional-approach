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

def firstnArmstrongNumbers(count):
    ac=0
    n=1
    while True:
        if isArmstrong(n):
            print(n)
            ac+=1
            if ac==count:
                break
        n+=1

firstnArmstrongNumbers(15)

