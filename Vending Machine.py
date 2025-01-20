
# -----VENDING MACHINE COMMENTS-----

# This is a dictionary containing all the items stored in the vending machine.
# It contains the item code for user reference, the item iteself, price, and lastly the stock.

items_list = {
    "101": {"Item_name": "Mango Juice", "Price": 5.50, "Stock": 10},
    "102": {"Item_name": "Watermelon Juice", "Price": 5.50, "Stock": 9},
    "103": {"Item_name": "Peach Juice", "Price": 5.50, "Stock": 10},
    "104": {"Item_name": "Dr Pepper", "Price": 7, "Stock": 0},
    "105": {"Item_name": "Mountain Dew", "Price": 6, "Stock": 9},
    "106": {"Item_name": "Iced Tea", "Price": 10, "Stock": 5},
    "107": {"Item_name": "Water", "Price": 2, "Stock": 10},
    "108": {"Item_name": "Cola", "Price": 8, "Stock": 3},
    "109": {"Item_name": "7UP", "Price": 7, "Stock": 10},
    "110": {"Item_name": "Chicken Sandwich", "Price": 10, "Stock": 5},
    "110": {"Item_name": "Beef Sandwich", "Price": 10, "Stock": 7},
}


# Prints ("\n ***** VENDING MACHINE *****")
print("\n ***** VENDING MACHINE *****")


# This prints the menu titles (Code, Item_name, Price, Stock)
print(f"{'Code':<10}{'Item_name':<20}{'Price':<10}{'Stock':<10}")
print("-"*50)

# This is a for statement. It take the information from items_list and prints the item information under the titles (Code, Item_name, Price, Stock)
for code, itemList in items_list.items():
    print(f"{code:<10}{itemList['Item_name']:<20}{
          itemList['Price']:<10}{itemList['Stock']:<10}")

# This is a while loop. It prints "Hello!, Please Enter the Product ID: " which asks the user to input the ID of an item they want to buy.
while True:

    # Prints(Hello!, Please Enter the Product ID: ")
    ProductID = input("\nHello!, Please Enter the Product ID: ")

    # It is followed by an if statement which checks if the ProductID entered is from the actual items_list.
    if ProductID in items_list:
        Item = items_list[ProductID]
        print(f"\n{items_list[ProductID]['Item_name']}")
        print(f"\nPrice: ${Item['Price']}")
        break
    else:
        # If the code entered is not on the list, it asks the user to try again!
        print("\nInvalid ID. Please try again.")


# Prints ("\nSelect a payment method (Cash/Card): ")
Payment = input("\nSelect a payment method (Cash/Card): ")


# This is an If statement with a while loop for payment verification.

# If the payment is done by 'Cash', it runs this if statement...
if Payment == "Cash":
    while True:
        try:

            # In this code, the user is asked to input an amount. It makes sure the amount is a numeric value.
            Paid = float(input(f"\nPlease Insert ${
                items_list[ProductID]['Price']} in Cash: "))
            if Paid == Item['Price']:
                # In this if statement, if the payment is correct and matches the price, it confirms the payment and prints ('\nPayment Successful!')
                print('\nPayment Successful!')
                print("\n Dispensing Item...")
                print("\n***Enjoy and have a great day!***")
                break  # This function breaks the loop

            # If the paid amount is greater then 'Price', the elif statement runs function to return change to user
            elif Paid > Item['Price']:

                # To return change, this code subtracts paid amount with actual item price.
                return_change = Paid - Item['Price']
                # Prints (Balance: $Amount)
                print(f"\nBalance: ${return_change:.2f}")
                print("\n Dispensing Item...")  # Prints (Dispensing Item...)
                # Prints(***Enjoy and have a great day!***")
                print("\n***Enjoy and have a great day!***")
                break
            else:
                # Prints (Insufficient Amount) if the amount is not the same as Item_list['Price']
                print("\n Insufficient Amount")
        except ValueError:
            # If the user enters an amount in anything other than numerical value, it prints ("\n Invalid input. Amount can only be a numeric value!")
            print("\n Invalid input. Amount can only be a numeric value!")

# If the payment is done by 'Card', it runs this elif statement..
elif Payment == "Card":
    # Prints (Processing Card Payment. Please Wait!)
    print("\nProcessing Card Payment. Please Wait!")
    print("\nPayment Successful!")  # Prints (Payment Successful!)
    # Prints (***Enjoy and have a great day!***)
    print("\n***Enjoy and have a great day!***")
else:
    # If there is an input error, it prints(Invalid Payment Option!)
    print("Invalid Payment Option!")
