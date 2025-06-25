def calculate_gross_salary(salary,benefits):
        Gross_salary = salary + benefits
        return Gross_salary
salary = float(input("Enter basic Salary: "))
benefits = float(input("Enter Benefits"))
gross = calculate_gross_salary(salary,benefits)
print(gross)

def nssf_rate(gross):
    if gross >= 18000:
        nssf_rate = gross * 6/100
        result = f"Your Nssf rate = {nssf_rate} "
        return result
    else:
         denied = "Minimum of 18000 is required."
         return denied
gross = calculate_gross_salary(salary,benefits)
NSSF = nssf_rate(gross)
print(NSSF)


