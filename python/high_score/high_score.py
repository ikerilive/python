# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
max_number = student_scores[0]

for number in student_scores:
    if number > max_number:
        max_number = number
        
print(f"The highest score in the class is: {max_number}")