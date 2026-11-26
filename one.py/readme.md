# Grocery Store Management System

## Project Description

The **Grocery Store Management System** is a simple Python project used to manage grocery items, prepare bills, calculate discounts and GST, and maintain the available stock.

The program allows the user to select grocery items, enter quantities, check stock availability, calculate the total bill, and save the generated bill in a text file.

## Language Used

- Python 3

## Concepts Used

- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Input and Output
- File Handling
- Basic Billing Calculation

## Features

1. View available grocery stock.
2. Create a new customer bill.
3. Check whether an item is available.
4. Check whether enough stock is available.
5. Automatically reduce stock after a purchase.
6. Calculate subtotal.
7. Apply a 10% discount when the subtotal is ₹1000 or more.
8. Calculate 5% GST.
9. Calculate the final bill amount.
10. Save the bill in `bills.txt`.

## Available Items

| Item | Price | Stock |
|---|---:|---:|
| Rice | ₹50 | 100 |
| Sugar | ₹45 | 50 |
| Milk | ₹30 | 40 |
| Oil | ₹150 | 20 |

## Discount Rule

If the subtotal is **₹1000 or more**, a **10% discount** is applied.

If the subtotal is less than ₹1000, no discount is applied.

## GST Rule

After applying the discount, **5% GST** is calculated.

### Formula

```text
Discount = Subtotal × 10 / 100

Amount After Discount = Subtotal - Discount

GST = Amount After Discount × 5 / 100

Total = Amount After Discount + GST
```

## How to Run the Project

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Save the Code

Save the Python program as:

```text
grocery_store.py
```

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python grocery_store.py
```

## Main Menu

When the program starts, it displays:

```text
===== GROCERY STORE MANAGEMENT SYSTEM =====
1. New Bill
2. View Stock
3. Exit
```

### Option 1: New Bill

Select option `1` to create a new bill.

Enter the item name and quantity.

Example:

```text
Enter item name: Rice
Enter quantity: 2
```

The program adds the item to the bill and reduces the available stock.

### Option 2: View Stock

Select option `2` to see the current stock.

Example:

```text
----- CURRENT STOCK -----
Rice: 100
Sugar: 50
Milk: 40
Oil: 20
```

### Option 3: Exit

Select option `3` to close the program.

## Error Handling

The program handles some common errors.

### Item Not Found

If the user enters an item that is not available:

```text
Item 'Butter' not found in inventory.
```

### Insufficient Stock

If the requested quantity is greater than the available stock:

```text
Insufficient stock for Milk. Available: 40
```

### Invalid Quantity

If the user enters something other than a number for quantity:

```text
Please enter a valid quantity.
```

## File Handling

The generated bills are stored in:

```text
bills.txt
```

The program uses append mode so that new bills are added without deleting previous bills.

```python
with open("bills.txt", "a") as file:
```

## Example

Suppose the customer purchases:

```text
Rice = 2
Milk = 3
```

Calculation:

```text
Rice = 2 × ₹50 = ₹100
Milk = 3 × ₹30 = ₹90

Subtotal = ₹190
Discount = ₹0
GST = ₹9.50

Total = ₹199.50
```

Output:

```text
Subtotal: 190.00
Discount(0%): 0.00
GST(5%): 9.50
Total: Rs. 199.50
```

## Project Structure

```text
Grocery-Store-Management-System/
│
├── grocery_store.py
├── bills.txt
└── README.md
```

## Learning Outcomes

After completing this project, we can understand:

- How to use Python dictionaries and lists.
- How to create and call functions.
- How to use loops and conditions.
- How to perform billing calculations.
- How to check and update stock.
- How to handle invalid user input.
- How to store information in a text file.
- How to create a basic Python-based management system.

## Conclusion

The Grocery Store Management System is a basic Python application that demonstrates important Python programming concepts such as **lists, dictionaries, functions, conditional statements, loops, billing calculations, and file handling**.

It can be further improved by adding a database, customer details, login system, product search, invoice numbers, and a graphical user interface.