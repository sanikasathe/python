# List of numbers
numbers = [34, 7, 23, 32, 5, 62]
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Print the sorted list
print("Sorted numbers:", numbers)
