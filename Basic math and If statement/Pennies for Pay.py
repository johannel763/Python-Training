## Calculates the amount of money a person would earn over a period of time
## if their salary is one penny the first day, two on the second and continues to double each day.

## Asks the user for a number of days

## Display a table showing what the salary was for each day and then show the total pay at the end of the period.

day_counter = 0
days = int(input('Enter an amount in days: '))
pay = float(0)

for x in range(days):
    day_counter += 1
    pay += .01
    print('Days: ', day_counter, '\t', 'Pay: $', round(pay, 2))

print('Total pay: $', round(pay, 2))