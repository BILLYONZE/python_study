# # Write a program that displays a numbers 1 to 50 inside a list.
# box = []
# numbers = list(range(1, 51))
# for i in numbers:
#     box.append(i)
# print(box)

# From 1 above display the ones divisible by 7 or 5 inside a list.
box = []
numbers =list(range(1, 51))
for num in numbers:
    if num % 7 == 0 or num % 5 == 0:
        box.append(num)
print(box)

# Find sum and average of values in the range between 10 to 40.
nums =list(range(10, 41))
total = 0
for i in nums:
    total = total + i
print("Sum of numbers is: ", total)
average = total/len(nums)
print(f"The average ={average}")

# Put in a list the first 10 odd numbers between 10 to 50. 
odd_nums = []
no = list(range(10,51))
for i in no:
    if i % 2 !=0:
        odd_nums.append(i)
        if len(odd_nums) == 10:
            break
print(odd_nums)
# or
odd_nums = []
no = list(range(10,51))
count=0
for i in no:
    if i %2 !=0:
        count = count + 1
        if count == 10:
         break
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# get input
# convert to int
# create a list upto 10
# loop the list
# print()
numbers = int(input("Type a number: "))
new=[]
mult = list(range(0,11))
for n in mult:
    new.append(mult)
    mult = numbers * n
    print( f"{numbers} * {n} =  {mult}")


# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
numb=list(range(1,51))
x = []
count = 0
for i in numb:
    if i % 2==0:
        x.append(i)
        count = count + 1
print(x)
print(count)

    
# ls1 = [ (“Jay”, "20"), (“Mo”,"30"), (“Mya”, "32") ]
# Display the total quantity of the 3 above.
ls1 = [("Jay", "20"),("Mo","30"),("Mya", "32")]
total = 0
for i in ls1:
    i = list(i)
    i[1]= int(i[1])
    total = total+i[1]
print(f"the total = {total}")
 #example