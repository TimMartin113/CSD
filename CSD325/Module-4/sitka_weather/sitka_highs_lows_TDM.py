"""
CSD 325 Assignment 4.2
Timothy Martin
June 23, 2026

This program provides an interactive interface for Sitka weather data.
It allows users to choose between visualizing daily high temperatures, daily low 
temperatures, or exiting the application. Data is dynamically read from a local 
CSV file and plotted as a line graph using the Matplotlib library.

"""


import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

def display_highs():
    filename = 'CSD325/Module-4/sitka_weather/sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)

    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def display_lows():
    filename = 'CSD325/Module-4/sitka_weather/sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, lows = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            low = int(row[6])
            lows.append(low)

    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

while True:
    print("Sitka Weather Menu")
    print("Option 1: High Temps")
    print("Option 2: Low Temps")
    print("option 3: Exit")

    choice = input("Select an option: ")

    if choice == "1":
        display_highs()
    elif choice == "2":
        display_lows()
    elif choice == "3":
        print("Thank you for using Sitka Weather History. Goodbye.")
        break
    else:
        print("Invalid option. Please try again.")
        
