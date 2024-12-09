## Uses a loop to display the number of calories burned after periods of time.

counter = 5

for time in range(10, 35, 5):
    counter += 5
    calories = counter * 4.2
    
    
    print(time, '\t', calories )