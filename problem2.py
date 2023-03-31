def takeinput():
    a=int(input("1st Number: "))
    b=int(input("2nd Number: "))
    opr=input("Operator: ")
    if opr=='+':
        displayResult(a,b,opr,a+b)
    elif opr=='*':
        displayResult(a,b,opr,a*b)
    elif opr=='-':
        displayResult(a,b,opr,a-b)
    elif opr=='/':
        displayResult(a,b,opr,a/b)
def displayResult(a,b,c,d):
    print(a,c,b,"=",d)

takeinput()


