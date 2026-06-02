# Assignment Name: CSD 205 Module 4.2 Assignment
# Author: Timothy Martin
# Date: 04/08/2026

# Description:
# This program converts miles to kilometers.
# It asks the user for miles, checks for valid input,
# then uses a function to perform the conversion.

# Function to convert miles to kilometers
def convert_miles_to_km(miles):
    return miles * 1.60934


# Main message
print("Miles to Kilometers Converter")

# Get user input with validation
while True:
    try:
        miles = float(input("Enter the number of miles driven: "))
        
        if miles < 0:
            print("Miles cannot be negative. Please try again.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")

# Call function
kilometers = convert_miles_to_km(miles)

# Display results
print(f"Miles driven: {miles:.2f}")
print(f"Kilometers: {kilometers:.2f}")