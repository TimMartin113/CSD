
# Assignment Name: CSD 205 Module 2.2 Assignment 
# Author: Tj Martin
# Date: 04/01/2026

# Description:
# This program calculates the cost of installing fiber optic cable based on the number of feet entered by the user.
# The cost per foot pricing is determined by bulk discount tiers:
# Over 500 feet: $0.50 per foot
# Over 250 feet: $0.70 per foot
# Over 100 feet: $0.80 per foot
# 100 feet or less: $0.87 per foot. 
# The program then displays the total cost.


# Display welcome message
print("Welcome to Fiber Optic Installation Cost Calculator")
print("Brought to you by: NorthWest Inland Fiber Solutions")
print("The more you buy the more you save!")

# Get user input
company_name = str(input("Enter your company name: "))
feet = float(input("Enter the number of feet of fiber optic cable to install: "))

# Determine cost per foot using if/elif/else
if feet >= 500:
    cost_per_foot = 0.50
elif feet >= 250:
    cost_per_foot = 0.70
elif feet >= 100:
    cost_per_foot = 0.80
else:
    cost_per_foot = 0.87

# Calculate total cost
total_cost = feet * cost_per_foot

# Display results
print(f"Installation Summary for: {company_name}")
print(f"Feet of cable: {feet:.2f}")
print(f"Cost per foot: ${cost_per_foot:.2f}")
print(f"Your total cost is: ${total_cost:.2f}")