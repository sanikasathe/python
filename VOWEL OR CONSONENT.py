# Taking input 
char = input("Enter a character: ").lower()

# Check if the character is a vowel
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():  # Check if it's a consonant
    print(f"{char} is a consonant.")
else:
    print("Please enter a valid alphabet character.")
