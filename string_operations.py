
fruit = "I like to eat mango"
str1 = "dkte"

# Printing string lengths
print(len(fruit))  
print(len(str1))   

# Using slice operator 
print(fruit[2:6])    # Extracts characters from index 2 to 5
print(fruit[-6:-1])  # Extracts the last 5 characters from 'fruit'

# string functions
print(fruit.capitalize())  # Capitalizes the first character
print(fruit.endswith('o')) # Checks if the string ends with 'o'
print(fruit.lower())       # Converts the string to lowercase
print(fruit.upper())       # Converts the string to uppercase
print(fruit.find('e'))     # Finds the position of the first occurrence of 'e'
print(fruit.count('e'))    # Counts the occurrences of 'e'
print(fruit.startswith('I')) # Checks if the string starts with 'I'
print(fruit.replace('mango', 'apple'))  # Replaces 'mango' with 'apple'

# String concatenation
print(str1 + fruit)  # Concatenates 'str1' and 'fruit'

# Additional string slicing example
str3 = 'apple'
str4 = 'clg'

# Extracting the second-to-last and last character from 'str3'
print(str3[-3:-1])  # Extracts 'pl' from 'apple'
