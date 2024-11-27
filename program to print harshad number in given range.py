def isHarshad(n):
    while True:
        dummy=n
        summ=0
        while dummy>0:
            rem=dummy%10
            dummy//=10
            summ+=rem
        if n%summ==0:
            return True
        else:
            return False

def harshadNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isHarshad(i):
            print(i)

harshadNumbers(1,100)

