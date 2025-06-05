# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct marks: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks = input("Enter Students Marks: ")
marks = int(marks)
if marks > 79:
    grade =f"A:{marks}"
elif marks >= 60:
    grade = f"B:{marks}"
elif marks >49:
    grade = f"C:{marks}"
elif marks >40:
    grade = f"D:{marks}"
else:
    grade = f"E:{marks}"
print(grade)
