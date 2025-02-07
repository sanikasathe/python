
# Initializing two lists
list = ['hi', 'bye', 22, 3]  # List of strings and integers
num = [50, 20, 14, 68, 14]   # List of integers

# Print the length of 'list'
print(len(list))  

# Concatenate 'list' and 'num' and store in 'list2'
list2 = list + num
print(list2)  

# Print 'num' repeated twice
print(num * 2)  

# Check if 50 is in 'num'
print(50 in num)  

# Append 70 to the end of 'list'
list.append(70)
print(list)  

# Extend 'num' by adding multiple elements [39, 42, 90]
num.extend([39, 42, 90])
print(num)  

# Remove the element 'hi' from 'list'
list.remove('hi')
print(list)  
# Pop the element at index 1 from 'num' (this removes the element 20)
num.pop(1)
print(num)  

# Count how many times 14 appears in 'num'
count1 = num.count(14)
print(count1)  

