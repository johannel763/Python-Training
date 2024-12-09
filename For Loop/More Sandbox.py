







star = '*'
how_many = int(input('How many rows of stars do you want? '))
counter = how_many

for x in range(how_many):
    counter -= 1
    line = star * counter
    print(line)

star = '*'
how_many = int(input('How many rows of stars do you want? '))
counter = 0

for x in range(how_many):
    counter += 1
    line = star * counter
    print(line)
















