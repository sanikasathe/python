

# Initialize the string 
str = 'hello'

# Initialize another string 
str1 = '10'

# Print the first character of the string 'str' (index 0)
print(str[0])  

# Print the second character of the string 'str' (index 1)
print(str[1])  

# Print the third character of the string 'str' (index 2)
print(str[2])  

# Print the fourth character of the string 'str' (index 3)
print(str[3])  

# Print the fifth character of the string 'str' (index 4)
print(str[4])  

# Print a substring from index 0 to 3 (not including index 3)
print(str[0:3])  

# Print a substring from index 0 to 4 with a step of 3 (i.e., taking every third character)
print(str[0:4:3])  

# Print a substring from index -5 to -2 with a step of 2 (negative indices count from the end)
print(str[-5:-2:2])  

# Print the length of the string 'str'
print(len(str))  

# Capitalize the first letter of the string (first letter in uppercase, the rest in lowercase)
print(str.capitalize()) 

# Convert the entire string to uppercase
print(str.upper())  

# Convert the entire string to lowercase
print(str.lower())  

# Check if the string ends with 'u'
print(str.endswith('u')) 

# Check if the string starts with 'h'
print(str.startswith('h')) 

# Count the number of occurrences of the character 'o' in the string
print(str.count('o'))  

# Check if all characters in the string are in lowercase
print(str.islower())  

# Check if all characters in 'str1' (which is '10') are digits
print(str1.isdigit()) 

# Find the index of the first occurrence of the character 'l' in the string
print(str.find('l'))  

# Replace the substring 'hello' with 'bye' in the string
print(str.replace('hello', 'bye')) 

# Concatenate the two strings 
print(str + str1)  

