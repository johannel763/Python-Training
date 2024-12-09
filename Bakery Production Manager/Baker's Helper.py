
print("Soft Round Rolls (rr)")
print("Hotdogs (h)")
print("Jumbo Hamburger Rolls (j)")

user_choice = str(input("What would you like to calculate? "))

## Soft Round Calculation
if user_choice == str("rr"):
    
    number_packets = int(input("How many packets do you require? "))

    cuts = number_packets * 6 / 20

    trays = cuts

    print(cuts, "number of 2.4kg cuts required")
    print(trays, "trays required")

## Hotdogs Calculation

elif user_choice == str("h"):
     
     number_packets = int(input("How many packets do you require? "))
     
     total_rolls = number_packets * 6
     
     cuts = number_packets * 6 / 20
     trays = total_rolls / 24
     
     print(cuts, "number of 2.4kg cuts required")
     print(trays, "trays required")

     print(total_rolls)

## Jumbo Hamburger Rolls

elif user_choice == str("j"):
     number_packets = int(input("How many packets do you require? "))

     total_rolls = number_packets * 6

     cuts = number_packets * 6 / 20
     trays = round(total_rolls / 18)

     print(cuts, "number of 3kg cuts required")
     print(trays, "trays required (3 x 5)")

     ##!!!! Add While loop which asks if another calculation is necesarry.