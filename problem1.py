patient_name=input("Enter patient's name: ")
cp=input("Was cleaning performed?(y/n):")
cf=input("Was cavity-filling performed?(y/n):")
x=input("Was X-Ray performed?(y/n):")
sub_amount=0
if cp=='y':
    sub_amount+=60
if cf=='y':
    sub_amount+=200
if x=='y':
    sub_amount+=100
tax=.15*sub_amount
dis=0
total=sub_amount+tax
if total>200:
    dis=.05*total
if total>300:
    dis=.1*total

print("\t\t\t\t  Melanie Denatal Clinic\n\t\t\t\t*------------------------*")

print("\n\t\t\t\tReceipt for patient name:"+patient_name)
print("\t\t\t---------------------------------------------\n")
print("\t\t\t\t\tSubtotal:",sub_amount)
print("\t\t\t\t\tTax:",tax)
print("\t\t\t---------------------------------------------\n")
print("\t\t\t\t\tTotal:",total-dis)
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
    print("Output is ",c)

takeinput()
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

pennies=int(input("Enter the number of pennies: "))
nickels=int(input("Enter the number of nickels: "))
dimes=int(input("Enter the number of dimes: "))
quarters=int(input("Enter the number of quarters: "))
totalcent= pennies*PENNY_VALUE + NICKEL_VALUE*nickels + dimes*DIME_VALUE + quarters*QUARTER_VALUE
totalDollars=totalcent/PENNIES_IN_DOLLAR
if totalDollars>1:
    print("Sorry, the amount you entered was more than one dollar.")
elif totalDollars<1:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("""Congratulations!
The amount you entered was exactly one dollar!
You win the game!!
  """)


