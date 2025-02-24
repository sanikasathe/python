# Taking input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Display the result
print(f"The factorial of {num} is {factorial}.")
