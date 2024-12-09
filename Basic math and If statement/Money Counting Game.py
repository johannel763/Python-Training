## The user enters an amount of coins to try and make up $1 exactly. If the result is not $1
## a message is displayed that tells the user whether it was more or less than a dollar.


penny_choice = int(input("How many pennies would you like? "))
nickel_choice = int(input("How many nickels would you like? "))
dime_choice = int(input("How many dimes would you like? "))
quarter_choice = int(input("How many quarters would you like? "))


penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

penny_total = (penny_choice * penny)
nickel_total = (nickel_choice * nickel)
dime_total = (dime_choice * dime)
quarter_total = (quarter_choice * quarter)

print("Pennies: $",penny_total)
print("Nickels: $",nickel_total)
print("Dimes: $",dime_total)
print("Quarters: $",quarter_total)

total = (penny_total + nickel_total + dime_total + quarter_total)

if total < 1:
    print("$", total, "is not quite a full dollar!")
elif total > 1:
    print("$", total, "That's more than a dollar!")
elif total == 1:
    print("$", round(total), "That's a dollar!")