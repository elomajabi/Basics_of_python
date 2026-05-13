# Build a program that lets a user enter the prices of items. The program should keep track of the total cost and only stop when the user types "done".
total_price = 0.0
while True:
    input_field = input("Please enter the item's price: ")

    if (input_field.lower() == "done"):
        print(f"Your total price was {total_price}")
        break

    price = float(input_field)
    total_price += price