#need a dictionary and define in code .

menu  = {
    'samosa': 10,
    'chai': 15,
    'momos':40,
    'burger':50,
    'pizza':200,
    'coffee':60,

}
#print anything or Greet...
print("Welcome to our family restaurant")
print("samosa: RS10\nchai: RS15\nmomos: RS40\nburger: 50\npizza: RS200\ncoffee: RS60,")

# total order is 0 that's why we start with o amount .

Total_order = 0   #no order completed yet

# now start yor order ...
order1 = input("Enter the name of item you want to order = ")
if order1 in menu:
    Total_order += menu[order1]
    print(f"Your order {order1} has been added to your order")
else:
    print(f"Order item {order1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    order2 = input("Enter the name of other item = ")
    if order2 in menu:
        Total_order += menu[order2]
        print(f"Item {order2} has been added to order")
    else:
        print(f"Order item {order2} is not available!")

print(f"The total amount of items to pay is {Total_order}") #hello menu


