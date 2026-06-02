# CSD 205 Assignment 6.2
# Author: Timothy Martin
# Date: 04/22/26

# This program demonstrates:
# 1. Creating a tuple
# 2. Displaying tuple contents
# 3. Iterating through the tuple
# 4. Displaying values in reverse order

def main():
    # Initialize tuple with 20 elements from the periodic table
    elements = (
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
        "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
        "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus",
    )

    # Display entire tuple in one statement
    print("Here are the first 15 elements of the periodic table:")
    print(elements)

    print("\n Forward Order:")

    # Iterate through tuple (forward)
    for element in elements:
        print(f"{element} is an element on the periodic table.")

    print("\n Reverse Order:")

    # Iterate in reverse order
    for element in reversed(elements):
        print(f"Reviewing in reverse, {element} is an element.")


# Call main function
if __name__ == "__main__":
    main()