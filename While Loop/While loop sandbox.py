
choice = "y" 

while choice == "y":
    print('Another!')
    choice = str(input("Wanna go again? "))

print("Exited")

####################################################################################################

counter = 0

while counter < 500:
    counter += 1 
    print(counter)

print("Exited")


#####################################################################################################

proceed = "y"

while proceed == "y":

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
    
    proceed = str(input("Want to spin again? "))

    ##############################################################################################

    

