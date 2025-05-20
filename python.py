# Write a python program that:
# Accept a sentence from the user.input()
# Count the number of words in it
# Capitalize the first letter of each word
# write the sentance in reverse
sentence = input("Enter your sentence: ")
sentence_title = sentence.title()
print(sentence_title)
sentence_split = sentence.split(" ")
print (sentence_split)
# print(len(sentence)) is used to count the number of characters
print(len(sentence_split))
print (sentence[::-1])
# Convert text to "good habits are hard to break!"
# text = " BAD habits are hard to break! " 
text = " BAD habits are hard to break! "
text = text.strip()
text = text.replace("BAD", "good")
print(text)
# clean email, and extract domain 
# email ="  John.DOE@GMAIL.com  "
email ="  John.DOE@GMAIL.com  "
email = email.lower()
email = email.strip()
email_slice = email[9:18]
# "g ==9"
# "m" ==17
print(email_slice)
# split
email_split= email.split("@")
print(email_split[-1])
# in exctracting the domain which is "gmail.com" ia also DISPLAYED AT THE TERMINAL

# Clean sentences and create a formated sentence "My name is John Doeand I love reading Books"
# first = "john"
# last = "DOE"
# hobby = "  Reading Books  " 
first = "john"
first = first.capitalize()
last = "DOE"
last = last.capitalize()
hobby = "  Reading Books  " 
hobby_strip = hobby.strip()
# Using concatination Method
print ("My name is " + first + " " + last + " and I love " + hobby_strip)
# Using f-string method
print(f"My name is {first} {last} and I love {hobby_strip}")
