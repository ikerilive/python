# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize variables for the sum and count
total_height = 0
number_of_students = 0

# Loop through the heights to calculate the sum and count
for height in student_heights:
    total_height += height
    number_of_students += 1

# Calculate the average height
average_height = total_height / number_of_students

# Round the result to the nearest whole number
average_height_rounded = round(average_height)

# Print the results
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height_rounded}")
