# CSD 205 - Module 8 Assignment
# Author: Timothy Martin
# This program stores stock prices in a dictionary and allows the user to search for a ticker symbol

def main():
    # Dictionary of stock tickers and prices
    stocks = {
        "AAPL": 175.25,
        "MSFT": 320.10,
        "GOOGL": 2850.50,
        "AMZN": 135.75,
        "TSLA": 720.30,
        "NFLX": 410.20,
        "META": 295.60,
        "NVDA": 890.45,
        "INTC": 34.80,
        "AMD": 120.55
    }

    # Input validation loop
    ticker = input("Enter a stock ticker symbol: ").upper()

    while ticker not in stocks:
        print("Ticker symbol not found. Please try again.")
        ticker = input("Enter a stock ticker symbol: ").upper()

    # Display result once valid
    print(f"The current price of {ticker} is ${stocks[ticker]:.2f}")


# Call main function
main()