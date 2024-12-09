
for num in [1,2,3,4]:
    print(num)

##################################################################

display_number = 0 

for num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    display_number += 1
    print(display_number)


##################################################################

for name in ['Johan', 'Sue', 'Dan']:
    print(name)

##################################################################

for num in range(10):
    print(num)

##################################################################

for x in range(0, 50, 2):
    print(x)

##################################################################

print('Number', '\t', 'Square')
for x in range(0, 10):
    total = x **2
    print(x, '\t' ,total)

##################################################################

print('KPH', '\t', 'MPH')

for x in range(60, 320, 10):
    mph = x * 0.6214
    print(x, '\t', mph)

##################################################################

print('KPH', '\t', 'MPH')

START_SPEED = int(input("Enter the start speed: "))
END_SPEED = int(input('Enter the end speed: '))
INCREMENT = int(input('What increment would you like to set? '))
SPEED_FACTOR = 0.6214

for speed in range(START_SPEED, END_SPEED, INCREMENT):
    mph = speed * 0.6214
    print(speed, '\t', round(mph))

##################################################################



