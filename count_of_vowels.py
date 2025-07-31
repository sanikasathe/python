s = input("Enter a string: ")
count = 0
for i in range(len(s)):
    if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count += 1
print("Total number of vowels:", count)
