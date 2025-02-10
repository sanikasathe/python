# Create a dictionary with key-value pairs
dict = {
    "name": "sanika",   # key: "name", value: "sanika"
    "age": 19,          # key: "age", value: 19
    "village": "mugali" # key: "village", value: "mugali"
}

# Print the type of the dictionary
print(type(dict))  

# Print the dictionary
print(dict)  

# Print the length of the dictionary (number of key-value pairs)
print(len(dict))  

# Access and print the value associated with the key "name"
print(dict.get("name"))  

# Print all the keys in the dictionary
print(dict.keys())

# Print all the values in the dictionary
print(dict.values()) 

# Add a new key-value pair to the dictionary using the update method
dict.update({"color": "pink"})  # Adds the key "color" with value "pink" to the dictionary
print(dict)  # Displays the updated dictionary

# Print all the items (key-value pairs) in the dictionary
print(dict.items())  

# Check if the key "name" exists in the dictionary
if "name" in dict:
    print("yes")  
else:
    print("no")  

# Remove the key-value pair with the key "color"
dict.pop("color")  
print(dict) 

# Remove and return the last inserted key-value pair
dict.popitem()  
print(dict)  

# Create a copy of the dictionary
mydict = dict.copy()  
print(mydict)  
