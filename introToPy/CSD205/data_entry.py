# CSD 205 Assignment 5.2
# Author: Timothy Martin
# Date: 04/15/26

# This program will:
# 1. Ask the user for a file name
# 2. Ask for their personal information (name, address, phone)
# 3. Write the data to a file in comma-separated format
# 4. Read the file and display its contents

# Prompt the user to enter a file name
file_name = str(input("What would you like to name your file?:"))
full_file_name = file_name + "_data.txt"


# Prompt the user to enter their info
name = str(input("Please Enter your name: "))
address = str(input("Please enter your address: "))
phone = str(input("Please enter your phone number:"))

# Create a single line of text with:
# name, address, phone number (comma-separated)
user_data = name + "," + address + "," + phone + "\n"

# Open the file using the full file name in write mode ("w")
with open(full_file_name, "w") as file:
    file.write(user_data)

# Open the same file again, this time in read mode ("r")
with open(full_file_name, "r") as file:
    content = file.read()

# Display the contents to the user
print("Saved file content:")
print(content)
