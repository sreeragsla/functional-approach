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

def printHarshad(N):
    if isHarshad(N):
        print(N)

printHarshad(21)
