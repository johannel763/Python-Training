## This program asks a user to enter a name, the name is then added to a list, and
## the user is asked if he wants to add another name to the list.



add_another = "y"
name_list = []

while add_another == "y":

    name = str(input("Enter a name to add to the list: "))
    name_list.append(name)
    print(name_list)

    add_another = str(input("Do you want to add another name to the list? "))


##############################################################################
MAX_TEMP = int(103)
temperature = int(input("What is the temperature? "))

while temperature > MAX_TEMP:
    
    print("Temperature is too hot!")
    print("Turn down bunsen burner until temperature is below 103 degrees celcius.")
    temperature = int(input("What is the temperature? "))

print("Temperature is fine")

