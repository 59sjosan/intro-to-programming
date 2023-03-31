pateint_name=input("Enter pateints name:")
cp=input("Was cleaning performed?(y/N):")
cf=input("Was cavity-filling performed?(y/N):")
xray=input("Was x-ray performed?(y/N):")
sub_amount=0
if cp=='y':
    sub_amount+=60
if cf=='y':
    sub_amount+=200
if xray=='y':
    sub_amount+=100
    tax=0.15*sub_amount
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