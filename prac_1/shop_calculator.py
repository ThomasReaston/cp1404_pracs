"""Shop calculator to add up prices and items and apply a discount id required"""

def main():

    total = 0
    number_of_items = int(input("PLease enter the number of items:- "))
#Get the umber of items so can ask for each price

    for i in range(number_of_items):
        price = float(input("Enter the item price ($):- "))
        total += price
#Get user to enter prices

    if total >= 100:
        total = total*0.9
#Check if over $100 and apply discount

    print("For these ",number_of_items,"Your total is $",total)
#print total

main()






