## The program asks the user to enter an objact's mass, then calculates it's weight.
## if the object weighs more than 500 newtons, it's too heavy, and if it weighs less than 100 
## newtons, it's too light.

mass = float(input("Please enter a mass to convert to weight: "))

weight = float(mass * 9.8)

print(weight)

if weight > float(500):
    print("That's over 500 newtons!! Way too heavy!")
elif weight < float(100):
    print("Less than 100 newtons!! Way too light!")