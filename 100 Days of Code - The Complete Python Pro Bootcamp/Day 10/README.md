# Day 10: Functions with Outputs 🧮

Day 10 introduces functions that return values and culminates in building a fully functional calculator program with continuous operation capabilities.

## 📚 Topics Covered

### 1. Functions with Outputs
- Creating functions that return values
- Using the `return` statement
- Capturing and using function outputs

### 2. Multiple Return Values
- Functions that can return different values
- Early returns with conditional logic
- Handling multiple return scenarios

### 3. Docstrings
- Documenting functions with docstrings
- Writing clear function descriptions
- Best practices for code documentation

### 4. Calculator Project
- Building a complete calculator program
- Implementing continuous calculations
- Using dictionaries to store functions

## 🗂️ Exercises and Projects

### Practice Exercises:
1. **[Functions with Outputs](./Functions%20with%20Outputs/)** - Learn to return values from functions
2. **[Multiple Return Values](./Multiple%20Return%20Values/)** - Handle different return scenarios
3. **[Docstrings](./Docstrings/)** - Document your functions properly

### Main Project:
🧮 **[Calculator Project](./Calculator%20Project/)** - Build a fully functional calculator with continuous operation

## 🎮 Calculator Project Features

### Operations Supported:
- ➕ **Addition**: Add two numbers
- ➖ **Subtraction**: Subtract second number from first
- ✖️ **Multiplication**: Multiply two numbers
- ➗ **Division**: Divide first number by second

### Advanced Features:
- 🔄 **Continuous Calculation**: Use previous results for new calculations
- 🎨 **ASCII Art Logo**: Beautiful calculator interface
- 💾 **Memory Function**: Remember last result
- 🔄 **Restart Option**: Start fresh calculations anytime

### How to Run:
```bash
cd "Day 10/Calculator Project"
python main.py
```

## 🧠 Key Programming Concepts

### Functions with Return Values
```python
def add(n1, n2):
    """Add two numbers and return the result."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract n2 from n1 and return the result."""
    return n1 - n2

# Using the functions
result = add(5, 3)  # result = 8
```

### Storing Functions in Dictionaries
```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Using functions from dictionary
operation_symbol = "+"
result = operations[operation_symbol](5, 3)
```

### Multiple Return Values
```python
def format_name(f_name, l_name):
    """Format and return a properly capitalized full name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
```

## 🎯 Learning Objectives

By the end of Day 10, you should be able to:
- ✅ Create functions that return values
- ✅ Use the `return` statement effectively
- ✅ Handle multiple return scenarios
- ✅ Write proper docstrings for functions
- ✅ Store functions as dictionary values
- ✅ Build programs with continuous operation
- ✅ Create user-friendly interfaces

## 🔧 Advanced Function Concepts

### Early Returns
```python
def is_leap_year(year):
    """Check if a year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
```

### Function Documentation
```python
def calculate(n1, n2, operation):
    """
    Perform a mathematical operation on two numbers.
    
    Args:
        n1 (float): First number
        n2 (float): Second number  
        operation (str): Operation symbol (+, -, *, /)
        
    Returns:
        float: Result of the calculation
    """
    return operations[operation](n1, n2)
```

## 🎨 Calculator Program Flow

```
1. Display calculator logo
2. Get first number from user
3. Show available operations
4. Get operation choice
5. Get second number
6. Calculate and display result
7. Ask if user wants to continue:
   - Yes: Use result as first number, repeat from step 3
   - No: Start over from step 2
```

## 💡 Programming Best Practices

### Function Design:
- **Single Responsibility**: Each function should do one thing well
- **Clear Names**: Function names should describe what they do
- **Documentation**: Use docstrings to explain function purpose
- **Return Values**: Always return meaningful values

### Code Organization:
- **Modular Design**: Separate different functionalities
- **Reusable Functions**: Write functions that can be used multiple times
- **Clean Interfaces**: Make functions easy to use and understand

## 🏆 Challenges

Extend your calculator with these features:

1. **Easy**: Add more operations (power, square root, modulo)
2. **Medium**: Implement scientific calculator functions
3. **Hard**: Add memory functions (store, recall, clear)
4. **Expert**: Create a history feature that shows previous calculations

## 🔍 Code Examples

### Basic Calculator Structure:
```python
def calculator():
    """Main calculator function with continuous operation."""
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input("Type 'y' to continue or 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()  # Recursion to start over
```

## 🎓 What You've Learned

Day 10 represents a major milestone in your Python journey:

### Technical Skills:
- Function return values and outputs
- Dictionary-based function storage
- Program flow control and recursion
- User interface design

### Problem-Solving Skills:
- Breaking complex problems into functions
- Designing user-friendly interfaces
- Handling different user choices
- Creating reusable code components

**Next**: [Day 11 - The Blackjack Capstone Project](../Day%2011/)

---

**🧮 Sample Calculator Session:**
```
What's the first number?: 15
+
-
*
/
Pick an operation: +
What's the next number?: 7
15.0 + 7.0 = 22.0
Type 'y' to continue calculating with 22.0, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 3
22.0 * 3.0 = 66.0
```

*Happy Calculating! 🧮*
