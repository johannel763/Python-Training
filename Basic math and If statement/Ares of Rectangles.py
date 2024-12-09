## A simple app that asks for the length and width of two rectangles to calaculate it's area.
## The code will then compare the rectangles and tell us which is bigger.


## Rectangle One
rectangle_1_len = float(input('Please enter the length of the first rectangle: '))

rectangle_1_wid = float(input("Please enter the width of the first rectangle: "))

rectangle_1 = rectangle_1_len * rectangle_1_wid

## Rectangle Two
rectangle_2_len = float(input('Please enter the length of the second rectangle: '))

rectangle_2_wid = float(input("Please enter the width of the second rectangle: "))

rectangle_2 = rectangle_2_len * rectangle_2_wid


print("The area for rectangle one is, ", rectangle_1,)

print("The area for rectangle one is, ", rectangle_2,)

## If statement which calculates which rectangle is bigger.

if rectangle_1 > rectangle_2:
    print("Rectangle one is bigger")
else: print("Rectangle two is bigger.")