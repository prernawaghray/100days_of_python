# Coffee Machine Project ☕

A simulation of a coffee vending machine with inventory management, payment processing, and multiple drink options.

## 📖 Project Description

This is the **Day 15** project from the 100 Days of Code Python Bootcamp. The coffee machine simulates a real coffee vending machine that can make different types of coffee drinks, manage resources, process payments, and track profits.

## 🎮 How to Use

1. **Turn on the machine**: Run the program
2. **Choose a drink**: Type "espresso", "latte", or "cappuccino"
3. **Insert coins**: Enter quarters, dimes, nickels, and pennies
4. **Enjoy your coffee**: If payment is sufficient and resources are available
5. **Special commands**:
   - Type "report" to see current resources and money
   - Type "off" to turn off the machine

## 🚀 How to Run

```bash
# Navigate to the project directory
cd "100 Days of Code - The Complete Python Pro Bootcamp/Day 15/Coffee Machine Project"

# Run the coffee machine
python main.py
```

## 📁 Project Files

- **`main.py`** - Main coffee machine logic and user interaction
- **`solution.py`** - Complete solution reference

## ☕ Available Drinks

### Espresso - $1.50
- **Water**: 50ml
- **Coffee**: 18g
- **Milk**: 0ml

### Latte - $2.50
- **Water**: 200ml
- **Milk**: 150ml
- **Coffee**: 24g

### Cappuccino - $3.00
- **Water**: 250ml
- **Milk**: 100ml
- **Coffee**: 24g

## 🎨 Features

- **Resource Management**: Tracks water, milk, coffee, and money
- **Payment Processing**: Accepts quarters ($0.25), dimes ($0.10), nickels ($0.05), pennies ($0.01)
- **Change Calculation**: Returns exact change when overpaid
- **Inventory Checking**: Prevents orders when resources are insufficient
- **Profit Tracking**: Keeps track of total money earned
- **Admin Functions**: Report and shutdown commands

## 🧠 Programming Concepts Demonstrated

- **Dictionaries**: Storing drink recipes and machine resources
- **Functions**: Modular code organization
- **Input Validation**: Handling user choices and coin inputs
- **Conditional Logic**: Complex decision-making processes
- **Resource Management**: Tracking and updating inventory
- **Mathematical Operations**: Payment calculations and change

## 📝 Sample Usage

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.00 in change.
Here is your latte ☕️. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 50ml
Milk: 350ml
Coffee: 76g
Money: $2.50

What would you like? (espresso/latte/cappuccino): cappuccino
Sorry there is not enough water.

What would you like? (espresso/latte/cappuccino): off
```

## 🔧 Machine Resources

### Initial Resources:
```python
resources = {
    "water": 300,    # ml
    "milk": 200,     # ml
    "coffee": 100,   # g
}
```

### Coin Values:
```python
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01
```

## 🎯 Program Flow

```
1. Display menu options
2. Get user choice
3. If "report" → Show current resources and money
4. If "off" → Shutdown machine
5. If drink choice:
   a. Check if resources are sufficient
   b. Process payment
   c. Check if payment is sufficient
   d. Make coffee and deduct resources
   e. Return change if necessary
6. Repeat until "off" command
```

## 🎓 Learning Outcomes

After completing this project, you'll understand:

- **Complex Program Structure**: Managing multiple functions and data
- **Resource Management**: Tracking and updating inventory systems
- **Payment Processing**: Handling monetary transactions
- **User Interface Design**: Creating intuitive command-line interfaces
- **Error Handling**: Managing insufficient resources and payments
- **State Management**: Maintaining machine state across operations

## 🏆 Challenges

Try these extensions to enhance your learning:

1. **Easy**: Add a "refill" command to restock resources
2. **Medium**: Implement different cup sizes (small, medium, large)
3. **Hard**: Add a maintenance mode with cleaning cycles
4. **Expert**: Create a GUI version using Tkinter with buttons and displays

## 🔍 Key Programming Concepts

### Resource Checking Function
```python
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
```

### Payment Processing
```python
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
```

## 🛠️ Technical Implementation

The coffee machine uses:
- **Dictionary-based data storage** for recipes and resources
- **Modular function design** for different operations
- **Input validation** for user commands and coin inputs
- **State persistence** throughout the program execution
- **Mathematical precision** for monetary calculations

---

**Part of the 100 Days of Code - Python Bootcamp by Angela Yu**

*Enjoy your virtual coffee! ☕*
