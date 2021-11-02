#Tip, Tax, and Total
#Dominic Colella
#10/12/2021
import math

def main():
    print('This calculator will show you your meal with tax \
added and your tip based on the price of the meal')
    meal_price = meal_start()
    tax = meal_price * .06 #calculates tax value for addition to total later
    print('Here is your total with tax:')
    tax_total = round(meal_price + tax, 2)
    print(tax_total) #meal price with tax added
    print('Here is the tip based on the price of your meal:')
    meal_with_tip = meal_tip(meal_price)
    print(round(meal_with_tip, 2)) #tip value based on meal price
    meal_total = meal_with_tip + tax_total
    print('Your total with tax and tip added is below:')
    print(round(meal_total, 2))

#tax constant
sales_tax = .06

#tip values
tip_1 = .1
tip_2 = .13
tip_3 = .16
tip_4 = .19
tip_5 = .22

#Gets user input for base price of meal
def meal_start():
    meal_price = float(input('Enter the price of the meal $'))
    while meal_price < 0:
        print('Not possible.')
        meal_price = float(input('Enter the price of the meal $'))
    return meal_price

def meal_tip(meal_price):
    if meal_price >= 0.00 and meal_price <= 5.99:
        meal_with_tip = meal_price * .1
    elif meal_price >= 6.00 and meal_price <= 12.00:
        meal_with_tip = meal_price * .13
    elif meal_price >= 12.01 and meal_price <= 17.00:
        meal_with_tip = meal_price * .16
    elif meal_price >= 17.01 and meal_price <= 25.00:
        meal_with_tip = meal_price * .19
    else: 
        meal_price >= 25.01
        meal_with_tip = meal_price * .22
    return meal_with_tip

def meal_total():
     print(meal_total)

main()
