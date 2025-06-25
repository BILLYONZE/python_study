def calculate_gross_salary(salary,benefits):
        Gross_salary = salary + benefits
        return Gross_salary
salary = float(input("Enter basic Salary: "))
benefits = float(input("Enter Benefits"))
gross = calculate_gross_salary(salary,benefits)
print(gross)

def calculating_NHDF(gross):
    NHDF_cal = gross * 0.015
    result =f"Your NHDF = {NHDF_cal}"
    return result
NHDF = calculating_NHDF(gross)
print(NHDF)
