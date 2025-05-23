fruits= ["mangoes", "apples", "bananas","pineapples","grapes", "kiwis"]
# indexing
print(fruits[0])

#slicing
print(fruits[0:4])

my_list = [10,20,30,'Python','HTML']
my_list[4] = 'CSS'
my_list.append('Java')
# my_list.clear()
x = my_list.copy()
print(x)
my_list.insert(1, 100)
y=[1000,2000]
my_list.extend(y)
# my_list.index(100)
my_list.remove(1000)
my_list.pop(2)
my_list.reverse()
t = []
my_list.sort()
print(my_list)
grades = [100, 65, 32, 21, 65, 78]
grades.insert(2,["maths", "english", "kiswahili"])
grades.append("science")
grades.extend(["history", "geography"])
print (grades[2][2])
