target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

if 0 <= target <= 1000:
    
    sum = 0

for number in range(2, target + 1, 2):
    sum += number
print(sum)