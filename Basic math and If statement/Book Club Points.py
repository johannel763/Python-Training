## Program asks the user to enter number of books purchased this month, 
## then displays the number of points awarded

books_purchased = int(input("How many books have you purchased this month? "))

if books_purchased < 2:
    points = 0
elif books_purchased >= 2 and books_purchased <= 3:
    points = 5
elif books_purchased >= 4 and books_purchased <= 5:
    points = 15
elif books_purchased >= 6 and books_purchased <= 7:
    points = 30
elif books_purchased >= 8 and books_purchased <= 9:
    points = 60

print("You purchased", books_purchased, "books this month. You have earned", points, "points this month.")