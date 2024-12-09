## The program asks the user to enter a date in a mm/dd/yy format.
## If the month multiplied by the day equals the year, it is a magic number.

month = int(input("Please enter the month for example, 10: "))

day = int(input("Please enter the date for example 21: "))

year = int(input("Please enter the year for example 84: "))

if month * day == year:
    print("That's a magic date!")
else:
    print("Not a magic date")