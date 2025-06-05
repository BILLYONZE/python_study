# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:
salary = input("Enter Salary amount: ")
salary = int (salary)
benefits = input("Enter Benefits Accountable to: ")
benefits= int(benefits)
# Gross salary == salary + benefits
Gross_salary = salary + benefits 
if Gross_salary < 5999:
        nhif = 150
elif Gross_salary >= 6000 and Gross_salary <= 7999:
        nhif = 300
elif Gross_salary >= 8000 and Gross_salary <= 11999:
        nhif = 400
elif Gross_salary >= 12000 and Gross_salary <= 14999:
        nhif = 500
elif Gross_salary >=15000 and Gross_salary <= 19999:
        nhif = 600
elif Gross_salary >=20000 and Gross_salary <= 24999:
        nhif = 750
elif Gross_salary >= 25000 and Gross_salary <= 29999:
        nhif = 850
elif Gross_salary >= 30000 and Gross_salary <= 34999:
        nhif = 900
elif Gross_salary >= 35000 and Gross_salary <= 39999:
        nhif = 950
elif Gross_salary >= 40000 and Gross_salary <= 44999:
        nhif = 1000
elif Gross_salary >= 45000 and Gross_salary <= 49999:
        nhif = 1100
elif Gross_salary >= 50000 and Gross_salary <= 59999:
        nhif = 1200
elif Gross_salary >= 60000 and Gross_salary <= 69999:
        nhif = 1300
elif Gross_salary >= 70000 and Gross_salary <= 79999:
        nhif = 1400
elif Gross_salary >= 80000 and Gross_salary <= 89999:
        nhif = 1500
elif Gross_salary >= 90000 and Gross_salary <= 99999:
        nhif = 1600
else:
    nhif = 1700
print(nhif)

# print(f"Gross salary = {Gross_salary}")