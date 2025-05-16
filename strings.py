first_name="Billjoy"
second_name = "Mbaluka"
print (type(first_name))
# <class 'str'> is a string.
# Strings are a sequence of characters enclosed in quotes.
pi=22/7
r=7
area=pi*r**2
print(area,type(area))
#154.0 <class 'float'>
#floats are numbers with decimal points.
# The area of a circle with radius 7 is 154.0
# hence the area of a circle is a float.
x=True
print(type(x))
# <class 'bool'>
# Booleans are True or False values.
p=4
print(type(p))
# <class 'int'>
full_name = first_name + " " + second_name
print(full_name)
# Billjoy Mbaluka
# The + operator is used to concatenate strings.
x="1000"
y="2000"
print(x+y)
# 10002000
# The above is a string concatenation.
x=1000
y=2000
print(x+y)
# 3000
# The above is an integer addition.
# The + operator is used to add numbers.
# x = "1000"
# y = 2000
# print(x+y)
# # this gives a type error.

my_name = "Billjoy"
print(my_name[0])
# this is indexing

text="python programmer"
print(text[0:8])
print(text[7:17])
# this is slicing
# The above will print the characters from index 7 to 16.

# Below are some string methods.
# The string methods are used to manipulate strings.
my_text = "hELLO"
my_text =my_text.capitalize()
my_text= my_text.count("l")
print(my_text)
