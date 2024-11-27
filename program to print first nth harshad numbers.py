def isHarshad(n):
    while True:
        dummy=n
        summ=0
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem
        if n==summ:
            return True
        else:
            return False

def firstnHarshadNumbers(count):
    n=1
    hc=0
    while True:
        if isHarshad(n):
            print(n)
            hc+=1
            if hc==count:
                break
        n+=1
firstnHarshadNumbers(10)
