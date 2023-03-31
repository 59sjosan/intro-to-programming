def takeinput():
    a=int(input("1st Number: "))
    b=int(input("2nd Number: "))
    opr=input("Operator: ")
    if opr=='+':
        displayResult(a+b)
    elif opr=='*':
        displayResult(a*b)
    elif opr=='-':
        displayResult(a-b)
    elif opr=='/':
        displayResult(a/b)
def displayResult(c):
    print("Output is = ",c)

takeinput()


