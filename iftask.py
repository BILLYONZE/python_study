# # Take three inputs from a user, separately. Print the largest of the numbers.
# #     Hint: Determine what type of data is taken in as input
# number_1 = int(input("Enter a numbers of your choice : "))
# number_2 = int(input("Enter another number : "))
# number_3 = int(input("Enter the last number : "))
# if number_1 > number_2 and number_3 < number_1:
#     print(f"{number_1} is the largest number")
# elif number_2 > number_1 and number_3 < number_2:
#     print(f"{number_2} is the largest number")
# else :
#     print(f"{number_3} is the largest number")
# # Take four inputs from a user, separately. Print the largest of the numbers.
# #     Hint: Determine what type of data is taken in as input
# num1 = input("enter the first number: ")
# num1 = int(num1)
# num2 = input("enter the second number: ")
# num2 = int(num2)
# num3 = input("enter the third number: ")
# num3 = int(num3)
# num4 = input("enter the fourth number: ")
# num4 = int(num4)
# if num1>num2 and num1>num3 and num1>num4:
#     print(f"{num1} is the largest number")
# elif num2>num1 and num2>num3 and num2>num4:
#     print(f"{num2} is the largest number")
# elif num3>num1 and num3>num2 and num3>num4:
#     print(f"{num3} is the largest number")
# else:
#     print(f"{num4} is the largest number")
# # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# # if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# temp= input("what is the tempereratue like in your are?: ")
# temp=int(temp)
# if temp>30:
#     print("The temperature is too high")
# elif temp>15 and temp<30:
#     print("Normal temperature")
# else:
#     print("Cold temperature")
# # Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# # and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# x = input("x= ")
# x = int(x)
# y = input("y= ")
# y = int(y)
# if x>=10 and x<=20 and y>100:
#     print("Conditions met")
# else:
#     print("Conditions not met")

# #  Write a Python program that checks if a variable password is equal to the string "secret123".
# # If it is, print "Access   granted", otherwise print "Access denied"
# password = input("Enter your password: ")
# if password == "secret123":
#     print("Access granted")
# else:
#     print("Access denied")
# Write a Python program that checks if a variable student_score is greater than 90.
# If true, check if the attendance is greater than 80.
# If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = input("Enter your score: ")
student_score = int(student_score)
if student_score>90:
    print("Your score is good")
    attendance = input("Enter your attendance: ")
    attendance = int(attendance)
    if attendance>80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
    print("Your score is not good enough")

# # test
# dict = {"name": "Joe", "age": 30, "city": "New York"}
# if dict["name"] == "John":
#     print("true")
# else:
#     print("false")