## User enters number of packages purchased. The program should then display
## the amount of discount if any and the total payable after discount.

packages_sold = int(input("How many packages were sold? "))

package_price = int(99)

if packages_sold >= 10 and packages_sold <= 19:
    discount_given = float(packages_sold * package_price) * .10
elif packages_sold >= 20 and packages_sold <= 49:
    discount_given = float(packages_sold * package_price) * .20
elif packages_sold >= 50 and packages_sold <= 99:
    discount_given = float(packages_sold * package_price) * .30
elif packages_sold > 100:
    discount_given = float(packages_sold * package_price) * .40

sales_price = (packages_sold * package_price) - discount_given

print("Packages sold: ", packages_sold)
print("Gross: ", (packages_sold * package_price))
print("Discount given: ", discount_given)
print("Net Sale: ", sales_price)