# CSD 205 Assignment 3.2
# Author: Timothy Martin
# Date: 04/02/26

# Discription: This program calculates how many years it takes for an investment to double.
# It uses a while loop to repeatedly apply interest until the
# investment value reaches at least double the original amount.

#Welcome message
print("Want to know how long will it take to double your investment?")

# Get user input
initial_investment = float(input("Enter the investment amount: $"))
interest_rate = float(input("Enter the intrest rate (as a %):"))

#convert rate
rate = interest_rate / 100

# setup variables
resulting_value = initial_investment
years = 0

# loop for investment
while resulting_value < initial_investment * 2:
    resulting_value += resulting_value * rate
    years += 1

#Results Output
print("Investment Summary:")
print(f"Starting Amount: ${initial_investment:.2f}")
print(f"Intrest rate: {interest_rate}%")
print(f"Years to double: {years} Years")
print(f"Final Amount: ${resulting_value:.2f}")