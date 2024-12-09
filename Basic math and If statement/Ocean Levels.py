## Displays the number of mm that the ocean will have risin each year for the next 25 years.

years = 25
counter = 0

for x in range(years):
    counter += 1
    water_level = counter * 1.6
    print('Years: ', counter, '\t', 'Water level risen: ', round(water_level, 2))
