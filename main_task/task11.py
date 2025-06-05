# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
from datetime import datetime
current_time = datetime.now()
current_month= current_time.month
current_year =current_time.year
current_day =current_time.day
# print(current_time)
# print(current_day)
# print(current_month)
# print(current_year)
date_of_birth = input("enter your Birth date(dd/mm/yy): ")
date = date_of_birth.split("/")
print(f"{date} : Date of Birth")
years = current_year - int(date[2])
print(f"{years} Years")
months = current_month - int(date[1])
print(f"{months} Months")
days = current_day - int(date[0])
print(f"{days} Days")

if days<0:
    months = months - 1
    days = days + 30
    if months<0:
        years = years -1
        months = months + 12
print(f"You are {years} years, {months} months and {days} days old ")
