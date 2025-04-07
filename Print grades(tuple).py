#Q9
grades = tuple(float(input(f"Enter grade for subject {i+1}: ")) for i in range(5))

# Calculate the highest, lowest, and average grade
highest_grade = max(grades)
lowest_grade = min(grades)
average_grade = sum(grades) / len(grades)

# Print the results
print(f"Highest grade: {highest_grade:.2f}")
print(f"Lowest grade: {lowest_grade:.2f}")
print(f"Average grade: {average_grade:.2f}")
