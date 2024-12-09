## The app asks the user for a month as a number between 1 and 12

##The program should display whethr the month is in quarter one, two, three or four.

month = int(input('Please enter a month as a number: '))

if month >= 1 and month <= 3:
    print("Quarter 1")
elif month >= 4 and month <= 6:
    print("Quarter 2")
elif month >= 7 and month <= 9:
    print("Quarter 3")
elif month >= 10 and month <= 12:
    print("Quarter 4")
elif month < 0 or month > 12:
    print("ERROR!")