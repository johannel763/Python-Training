## Program keeps a running total of the amount of bugs caught
## in a five day period.


MAX_COUNT = 5
running_total = 0

for bugs in range(MAX_COUNT):
    num_bugs = int(input('Number of bugs: '))
    running_total += num_bugs

print('Total number of bugs collected: ', running_total)