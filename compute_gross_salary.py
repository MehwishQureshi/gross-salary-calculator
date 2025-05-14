"""Computation of gross salary"""

Basic = int(input("Enter basic amount : "))

grade = input("Enter grade among A,B and C : ")

if grade == 'A' :
    Allow = 1700
elif grade == 'B' :
    Allow = 1500
else :
    Allow = 1300

HRA = (20*Basic)/100

DA = (50*Basic)/100

PF = (11*Basic)/100

GrossSalary = Basic + HRA + DA + Allow - PF

print("Gross Salary is : ",GrossSalary)
