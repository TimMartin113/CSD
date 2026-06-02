# CSD 205 Assignment 7.2
# Author: Timothy Martin
# Date: 04/29/26

# This program asks the user for their first, middle, and last names
# and then displays their initials.

# Ask the user to enter their full name
full_name = input("Enter your first, middle, and last names: ")

# Split the name into parts
name_parts = full_name.split()

# Store each name in its own variable
first_name = name_parts[0]
middle_name = name_parts[1]
last_name = name_parts[2]

# Get the first letter of each name
first_initial = first_name[0].upper()
middle_initial = middle_name[0].upper()
last_initial = last_name[0].upper()

# Display the initials
print("Your initials are:", first_initial + ".", middle_initial + ".", last_initial + ".")
