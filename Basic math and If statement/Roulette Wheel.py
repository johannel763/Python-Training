## User picks a number from 1 to 36 and the program tells them whether the
## pocket is green, black or red.

##An error message should be displayed if the number is not between 1 and 36

user_choice = int(input("Pick a number from 1 to 36: "))

if user_choice < 0 or user_choice > 36:
    print("ERROR")
else:
    if user_choice >= 1 and user_choice <= 10:
        if (user_choice % 2) == 0:
            print(user_choice, "Black")
        else:
            print("Red")
    elif user_choice >= 11 and user_choice <= 18:
        if (user_choice % 2) == 0:
            print(user_choice, "Red")
        else:
            print(user_choice,"Black")
    elif user_choice >= 19 and user_choice <= 28:
        if (user_choice % 2) == 0:
            print(user_choice, "Black")
        else:
            print(user_choice, "Red")
    elif user_choice >= 29 and user_choice <= 36:
        if (user_choice % 2) == 0:
            print(user_choice, "Red")
        else:
            print(user_choice, "Black")