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