## A simple program that aks the user to enter an integer numbeer.
## The code then checks whether the numbeer is greater then, smaller than
## or equal to zero.

## HJ Nel

number = int(input("Please enter a number: "))

if number < 0:
    print("Negative")

elif number > 0:
    print("Positive")

else: print("Zero")