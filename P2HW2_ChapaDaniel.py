# ask the user to enter grades for each module
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

print("--------------------Results---------------------------")
# calculate and print the lowest grade
lowest = min(grade1, grade2, grade3, grade4, grade5, grade6)
print(f"Lowest Grade: {lowest}")

# calculate and print the highest grade
highest = max(grade1, grade2, grade3, grade4, grade5, grade6)
print(f"Highest Grade: {highest}")

# calculate and print the sum of grades
total = grade1 + grade2 + grade3 + grade4 + grade5 + grade6
print(f"Sum of Grades: {total}")

# calculate and print the average grade to two decimal places
average = total / 6
print(f"Average Grade: {average:.2f}")
print("------------------------------------------------------")
