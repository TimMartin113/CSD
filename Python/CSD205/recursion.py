# CSD 205 Assignment 11.1
# Author: Timothy Martin
# Date: 05/20/26
# This program compares a recursive and non-recursive
# approach to printing numbers from 1 to n.


# Recursive function
def recursive_count(n):
    # This function uses recursion to print numbers from 1 to n.
    # Base case: stop when n is 0
    if n == 0:
        return
    # Recursive call using a smaller value
    recursive_count(n - 1)
    # Print number after recursive call returns
    print(n)


# Non-recursive function
def loop_count(n):
    # This function uses a for loop to print numbers
    # from 1 to n without recursion.
    for i in range(1, n + 1):
        print(i)


# Main program
def main():
    print("Program START")

    # Input validation
    n = int(input("Enter a number greater than 0: "))

    while n <= 0:
        print("Invalid input. Try again.")
        n = int(input("Enter a number greater than 0: "))

    print("\nRECURSIVE OUTPUT")
    print("Recursive function START")
    recursive_count(n)
    print("Recursive function END")

    print("\nLOOP OUTPUT")
    print("Loop function START")
    loop_count(n)
    print("Loop function END")

    print("\nProgram END")


# Run program
if __name__ == "__main__":
    main()