## Asks the user for speed of a vehicle and the number of hours it has travelled.
## Display the distance for each hour travelled


hours = int(input('How many hours: '))
speed = int(input('How fast were you travelling? '))
counter = int(0)

print('Hour', '\t', 'Distance')
print('_______________________')

for time in range(hours):
    counter +=1
    distance = counter * speed
    
    print(counter, '\t', distance)









