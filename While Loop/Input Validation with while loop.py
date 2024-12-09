

temperature = int(input('Enter temperature:'))

while temperature < 0 or temperature is type(str):
    print('ERROR')
    temperature = int(input('Enter temperature:'))

counter = 5
running_total = 0

for x in range(counter):
    temperature = int(input('Enter temperature:'))
    running_total += temperature

average_temp = running_total / 6

print(running_total)
print(average_temp)
    

