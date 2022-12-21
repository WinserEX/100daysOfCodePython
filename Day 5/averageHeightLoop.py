# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
x = 0
i = 0
for stu in student_heights:
    x += stu
    i += 1
result = x/i
print(round(result))