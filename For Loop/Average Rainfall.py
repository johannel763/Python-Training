## Collects data and calculates average rainfall over a period of years.
## Program should ask number of years first.
## The outer loop will iterate once for each year.
## The inner loop will iterate twelve times, once for each month. It will also ask the user for rainfall in inches for that month.
## The program should display the number of months, total inches of rainfall, and average rainfall per month. for the entire period.


years = int(input('How many years of data do you wish to enter? '))

total_months = years * 12
total_rainfall = float(0)

for x in range(years):
    for y in range(total_months):
        rainfall = float(input('Reading in Inches: '))
        total_rainfall += rainfall
        average_rainfall = total_rainfall / total_months
    print('Total months: ', total_months)
    print('Total inches of rain: ', total_rainfall)
    print('Average monthly rainfall is ', average_rainfall, 'inches')


