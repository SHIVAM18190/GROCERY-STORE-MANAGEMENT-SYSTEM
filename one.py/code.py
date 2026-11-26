#NAME- SHIVAM KUMAR
#ERP- RU-26-02982
#SECTION- B2
#PS NO. - 51
#COURSE- BTECH CSE(CORE)
#TOPIC- GROCERY STORE MANAGEMENT SYSTEM


# Grocery Store Management System

# Inventory: item -> [price, stock]
inventory = {
    "Rice": [50, 100],
    "Sugar": [45, 50],
    "Milk": [30, 40],
    "Oil": [150, 20]
}


def view_stock():
    print("\n----- CURRENT STOCK -----")
    for item, details in inventory.items():
        print(item + ":", details[1])


def new_bill():
    cart = {}
    subtotal = 0

    while True:
        item = input("\nEnter item name (or 'done' to finish): ").strip().title()

        if item.lower() == "done":
            break

        if item not in inventory:
            print("Item '" + item + "' not found in inventory.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = inventory[item][0]
        stock = inventory[item][1]

        if quantity > stock:
            print("Insufficient stock for " + item +
                  ". Available: " + str(stock))
            continue

        # Add item to cart
        cart[item] = cart.get(item, 0) + quantity

        # Reduce stock
        inventory[item][1] -= quantity

        subtotal += price * quantity

        print(item, "added successfully.")

    # If no item was purchased
    if subtotal == 0:
        print("\nNo items purchased.")
        return

    # Discount
    if subtotal >= 1000:
        discount = subtotal * 10 / 100
        discount_text = "10%"
    else:
        discount = 0
        discount_text = "0%"

    amount_after_discount = subtotal - discount

    # GST 5%
    gst = amount_after_discount * 5 / 100

    total = amount_after_discount + gst

    # Display bill
    print("\n========== BILL ==========")

    for item, quantity in cart.items():
        price = inventory[item][0]
        amount = price * quantity
        print(item, "x", quantity, "=", amount)

    print("--------------------------")
    print("Subtotal:", format(subtotal, ".2f"))
    print("Discount(" + discount_text + "):",
          format(discount, ".2f"))
    print("GST(5%):", format(gst, ".2f"))
    print("Total: Rs.", format(total, ".2f"))
    print("==========================")

    # Save bill in file
    with open("bills.txt", "a") as file:
        file.write("\n========== BILL ==========\n")

        for item, quantity in cart.items():
            price = inventory[item][0]
            amount = price * quantity
            file.write(item + " x " + str(quantity) +
                       " = " + str(amount) + "\n")

        file.write("Subtotal: " + format(subtotal, ".2f") + "\n")
        file.write("Discount(" + discount_text + "): " +
                   format(discount, ".2f") + "\n")
        file.write("GST(5%): " + format(gst, ".2f") + "\n")
        file.write("Total: Rs. " + format(total, ".2f") + "\n")
        file.write("==========================\n")

    print("Bill saved successfully in bills.txt")


# Main Menu
while True:
    print("\n===== GROCERY STORE MANAGEMENT SYSTEM =====")
    print("1. New Bill")
    print("2. View Stock")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_bill()

    elif choice == "2":
        view_stock()

    elif choice == "3":
        print("Thank you for using Grocery Store Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
