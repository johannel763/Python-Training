import random

temperature = random.randint(1,45)

if temperature > 1 and temperature < 10:
    print("It's freezing today! Only", + temperature, "degrees")
    

elif temperature > 10 and temperature < 20:
    print("Only", temperature, "degrees today, quite chilly")

elif temperature > 20 and temperature < 30:
    print("Beautiful day today!" , temperature, "is the perfect temperature!")

else:
    print(temperature, "is too hot!")


