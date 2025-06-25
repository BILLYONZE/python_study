# gross function
def calculate_gross_salary(salary,benefits):
        Gross_salary = salary + benefits
        return Gross_salary
salary = float(input("Enter basic Salary: "))
benefits = float(input("Enter Benefits"))
gross = calculate_gross_salary(salary,benefits)
print(gross)

# nhif function
def calculate_nhif(gross):
        if gross < 5999:
                 nhif = 150
        elif gross >= 6000 and gross <= 7999:
                nhif = 300
        elif gross >= 8000 and gross <= 11999:
                nhif = 400
        elif gross >= 12000 and gross <= 14999:
                nhif = 500
        elif gross >=15000 and gross <= 19999:
                nhif = 600
        elif gross >=20000 and gross <= 24999:
                nhif = 750
        elif gross >= 25000 and gross <= 29999:
                nhif = 850
        elif gross >= 30000 and gross <= 34999:
                nhif = 900
        elif gross >= 35000 and gross <= 39999:
                nhif = 950
        elif gross >= 40000 and gross <= 44999:
                nhif = 1000
        elif gross >= 45000 and gross <= 49999:
                nhif = 1100
        elif gross >= 50000 and gross <= 59999:
                nhif = 1200
        elif gross >= 60000 and gross <= 69999:
                nhif = 1300
        elif gross >= 70000 and gross <= 79999:
                nhif = 1400
        elif gross >= 80000 and gross <= 89999:
                nhif = 1500
        elif gross >= 90000 and gross <= 99999:
                nhif = 1600
        else:
            nhif = 1700
        return nhif
NHIF = calculate_nhif(gross)
print(NHIF)

# NSSF function
def nssf_rate(gross):
    if gross >= 18000:
        nssf_rate = gross * 6/100
        result = f"Your Nssf rate = {nssf_rate} "
        return nssf_rate
    else:
         denied = "Minimum of 18000 is required."
         return denied
gross = calculate_gross_salary(salary,benefits)
NSSF = nssf_rate(gross)
print(NSSF)

# NHDF function
def calculating_NHDF(gross):
    NHDF_cal = gross * 0.015
    result =f"Your NHDF = {NHDF_cal}"
    return NHDF_cal
NHDF = calculating_NHDF(gross)
print(NHDF)

# taxable_income function 
def calculating_taxable_income(NSSF,NHDF,NHIF):
    taxable_income = gross - (NSSF + NHDF + NHIF)
    result = f"Your Taxable Income = {taxable_income}"
    return result
taxable_Income = calculating_taxable_income(NSSF,NHDF,NHIF)
print(taxable_Income)

# PAYEE function
def calculating_payee(taxable_Income):
       if taxable_Income <=24000 :
              result = f"10% => {taxable_Income}"
       elif taxable_Income - 24000 <= 8333 and taxable_Income - 24000 >= 467666:
              result = f"25% => {taxable_Income}"
       elif taxable_Income - 24000 - 8333  >= 467667 and taxable_Income - 24000 -8333 -467667 <=300000:
              result = f"30% => {taxable_Income}"
       elif taxable_Income - 24000 - 8333 - 467666 >= 300000 and taxable_Income - 24000 -8333 -467667 - 300000 <=800000:
              result = f"32.5% => {taxable_Income}"
       else:
            result = f"35% => {taxable_Income}"
            return result
PAYEE = calculating_payee(taxable_Income)
print(PAYEE)
