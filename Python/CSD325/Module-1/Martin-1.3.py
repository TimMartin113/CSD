# Timothy Martin
# CSD 325
# Assignment 1.3 - On the Wall + Flowchart(s)
# June 3, 2026

# This program asks the user for the number of bottles of beer on the wall and 
# then uses a function to count down to zero while displaying the song lyrics. 
# When the countdown ends, the program reminds the user to buy more beer.

def beer_countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.")
        bottles -= 1

    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.")


def main():
    bottles = int(input("Enter number of bottles: "))
    beer_countdown(bottles)
    print("Time to buy more beer.")


if __name__ == "__main__":
    main()
