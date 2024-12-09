## Displays a table of distances in miles and their equivalent in Kilometers

counter = 0




for x in range(0, 80, 10):
    counter += 10
    kilometers = counter * 1.60934
    print('Miles: ', counter, '\t', 'Km: ', round(kilometers,2))