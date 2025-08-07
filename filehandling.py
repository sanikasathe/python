#write mode
file1 = open("myfile.txt", "w")
file1.write("This is python file")
file1.close()

print("File written successfully.")

# read the file 
file2= open("myfile.txt", "r")
content = file2.read()
file2.close()

# Append mode
file3 = open("myfile.txt", "a")
file3.write("\nAppend operation successfull")
print("append successful")
file3.close()

# r+ mode: read and write (overwrite from beginning)
file = open("myfile.txt", "r+")
file.write("Start replaced using 'r+' mode.\n")
file.close()

# w+ mode: clear file, then write and read
file = open("myfile.txt", "w+")
file.write("Content written using 'w+' mode.\n")
file.seek(0)
content = file.read()
file.close()

print("File content after 'w+':")
print(content)

# 'a+' mode: Append and read (keeps old content)
file = open("myfile.txt", "a+")
file.write("Added line using 'a+' mode.\n")
file.seek(0)  # Move to start to read
content = file.read()
file.close()

# Print the file content on console
print("File content:")
print(content)
