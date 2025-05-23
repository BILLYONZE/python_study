x=99
y=5
# modulus (%) 4
q = x%y
print(q)
# floor(//) 19
z = x//y
print(z)
# exponentiation (**) 970299
a = x**3
print(a)
myvar = 1000
myvar = str(myvar)
print(type(myvar))
# <class 'str'>
myvar = int(myvar)
print(type(myvar))
# <class 'int'>
myvar = float(myvar)
print(type(myvar))
print(myvar)
# to get 2 inputs from the user and sum them up
length_A = int(input("Enter the length of A: "))
length_B = input("Enter the length of B: ")
length_B = int(length_B)
print(f"The total length of the values you chose is {length_A + length_B}")

# Questions
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
# round() function is used to round a number to the nearest integer or to a given number of
temp = round(temp)
temp = int(temp)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
temp = 56.8926
temp = str(temp)
print(temp[0:5])
# or
temp = float(temp)
temp=round(temp,2)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
temp = round(temp,3)
print(temp)
# or    
temp = str(temp)
temp = temp.replace("2","3")
print(temp[0:6])
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp = 56.8926
temp = str(temp)
temp = temp[3:]
temp = f"{temp[0]}.{temp[1:]}"
temp = float(temp)
print(temp)
# NB: Use string  slice & concatenation, but have result as float 

# convert 111.0789 to 78.9
temp = 111.0789
temp = str(temp)
temp = temp[4:]
# temp =f"{temp[1:3]}.{temp[3:]}"
temp = temp[1:3] + "." + temp[3:]
temp = float(temp)
print(temp)
