# Calculator Project 🧮

A fully functional calculator program with continuous operation capabilities and ASCII art interface.

## 📖 Project Description

This is the **Day 10** project from the 100 Days of Code Python Bootcamp. The calculator performs basic arithmetic operations and allows users to continue calculations with previous results or start fresh calculations.

## 🎮 How to Use

1. Enter the first number
2. Choose an operation (+, -, *, /)
3. Enter the second number
4. View the result
5. Choose to continue with the result or start a new calculation
6. Type 'n' to start over or 'y' to continue with the current result

## 🚀 How to Run

```bash
# Navigate to the project directory
cd "100 Days of Code - The Complete Python Pro Bootcamp/Day 10/Calculator Project"

# Run the calculator
python main.py
```

## 📁 Project Files

- **`main.py`** - Main calculator logic and user interaction
- **`art.py`** - ASCII art logo for the calculator
- **`solution.py`** - Complete solution reference

## 🎨 Features

- **Four Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Continuous Calculation**: Use previous results for new calculations
- **Input Validation**: Handles invalid operations gracefully
- **Clean Interface**: ASCII art logo and clear prompts
- **Memory Function**: Remembers the last result for continued operations

## 🧠 Programming Concepts Demonstrated

- **Functions with Return Values**: Creating functions that output results
- **Dictionaries**: Storing functions as values with operation symbols as keys
- **Function References**: Storing and calling functions from a dictionary
- **Recursion**: The calculator can call itself for continuous operation
- **Input Validation**: Checking for valid operations
- **Program Flow Control**: Managing different calculation paths

## 🎯 Calculator Operations

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```

### Supported Operations:
- **Addition (+)**: Adds two numbers
- **Subtraction (-)**: Subtracts second number from first
- **Multiplication (*)**: Multiplies two numbers
- **Division (/)**: Divides first number by second

## 📝 Sample Usage

```
  _____________________
 |  _________________  |
 | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
 | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
 |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
 | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
 | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
 | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
 | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
 | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
 | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
 | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
 | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
 |_____________________|

What's the first number?: 15
Pick an operation: +
What's the next number?: 7
15 + 7 = 22

Type 'y' to continue calculating with 22, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 3
22 * 3 = 66

Type 'y' to continue calculating with 66, or type 'n' to start a new calculation: n
```

## 🔧 Code Structure

### Main Functions:
```python
def add(n1, n2):
    """Add two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract n2 from n1"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divide n1 by n2"""
    return n1 / n2
```

### Dictionary of Operations:
```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```

## 🎓 Learning Outcomes

After completing this project, you'll understand:

- **Functions with Return Values**: How to create functions that return results
- **Dictionary Usage**: Storing functions as dictionary values
- **Function References**: Calling functions stored in data structures
- **Program Flow**: Managing different execution paths
- **User Experience**: Creating intuitive interfaces for programs
- **Code Organization**: Structuring programs with multiple functions

## 🏆 Challenges

Try these extensions to enhance your learning:

1. **Easy**: Add more operations (power, square root, modulo)
2. **Medium**: Implement memory functions (store, recall, clear)
3. **Hard**: Add support for multiple operations in one line (e.g., "5 + 3 * 2")
4. **Expert**: Create a graphical calculator interface using Tkinter

## 🔍 Key Programming Concepts

### Function Storage in Dictionaries
```python
# Instead of using if/elif chains:
if operation == "+":
    result = add(n1, n2)
elif operation == "-":
    result = subtract(n1, n2)

# Use dictionary lookup:
result = operations[operation](n1, n2)
```

### Recursive Program Flow
The calculator can call itself to start new calculations while maintaining clean code structure.

---

**Part of the 100 Days of Code - Python Bootcamp by Angela Yu**

*Happy Calculating! 🧮*
