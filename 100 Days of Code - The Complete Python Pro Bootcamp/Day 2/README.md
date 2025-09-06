# Day 2: Understanding Data Types and How to Manipulate Strings 🔢

Day 2 introduces you to Python's data types and teaches you how to work with numbers, perform mathematical operations, and manipulate strings effectively.

## 📚 Topics Covered

### 1. Data Types
- **Strings (str)**: Text data enclosed in quotes
- **Integers (int)**: Whole numbers without decimal points
- **Floats (float)**: Numbers with decimal points
- **Booleans (bool)**: True/False values

### 2. Type Error, Checking and Conversion
- Understanding type errors and how to fix them
- Using `type()` to check data types
- Converting between data types with `int()`, `float()`, `str()`
- Type casting and when to use it

### 3. Mathematical Operations
- Basic arithmetic operators: `+`, `-`, `*`, `/`
- Order of operations (PEMDAS/BODMAS)
- Integer division `//` and modulo `%`
- Exponentiation `**`

### 4. Number Manipulation and F-Strings
- Rounding numbers with `round()`
- Floor division and ceiling operations
- String formatting with f-strings
- Mathematical functions and shortcuts

## 🗂️ Exercises and Projects

### Practice Exercises:
1. **[Data Types](./Data%20Types/)** - Learn about different Python data types
2. **[Type Error, Checking and Conversion](./Type%20Error,%20Checking%20and%20Conversion/)** - Handle type errors and conversions
3. **[Mathematical Operations](./Mathematical%20Operations/)** - Perform calculations in Python
4. **[Number Manipulation](./Number%20Manipulation/)** - Work with numbers and formatting

### Main Project:
💰 **[Tip Calculator Project](./Tip%20Calculator%20Project/)** - Calculate tips and split bills among friends

## 🎮 Tip Calculator Project

The Day 2 capstone project is a practical tip calculator that:
- Calculates the total bill including tip
- Splits the bill among multiple people
- Handles different tip percentages
- Formats the output to show currency properly

### Project Requirements:
- Ask for the total bill amount
- Ask for the tip percentage (10%, 12%, or 15%)
- Ask for the number of people to split the bill
- Calculate and display each person's share

### Sample Interaction:
```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93
```

## 🧠 Key Programming Concepts

### Data Type Identification
```python
# Check data types
print(type("Hello"))     # <class 'str'>
print(type(123))         # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>
```

### Type Conversion
```python
# Converting between types
age = input("What's your age? ")  # Returns string
age = int(age)                    # Convert to integer
print(f"You are {age} years old")
```

### Mathematical Operations
```python
# Basic arithmetic
result = 10 + 5    # Addition: 15
result = 10 - 3    # Subtraction: 7
result = 4 * 6     # Multiplication: 24
result = 15 / 3    # Division: 5.0 (always returns float)
result = 15 // 4   # Floor division: 3
result = 15 % 4    # Modulo: 3
result = 2 ** 3    # Exponentiation: 8
```

### Number Formatting
```python
# Rounding numbers
price = 19.9333333
rounded_price = round(price, 2)  # 19.93

# F-string formatting
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
```

## 🎯 Learning Objectives

By the end of Day 2, you should be able to:
- ✅ Identify different Python data types
- ✅ Convert between data types when needed
- ✅ Perform mathematical calculations in Python
- ✅ Handle type errors effectively
- ✅ Use f-strings for string formatting
- ✅ Round numbers to specific decimal places
- ✅ Build a practical calculator application

## 🔧 Python Concepts Introduced

### PEMDAS/BODMAS Order of Operations
```python
# Python follows mathematical order of operations
result = 3 + 5 * 2    # Result: 13 (not 16)
result = (3 + 5) * 2  # Result: 16 (parentheses first)
```

### String Subscripting
```python
# Access individual characters in strings
name = "Python"
print(name[0])  # P (first character)
print(name[-1]) # n (last character)
```

### Common Type Errors
```python
# This will cause a TypeError:
# print("Number of letters: " + len("Hello"))

# Correct way:
print("Number of letters: " + str(len("Hello")))
# Or using f-strings:
print(f"Number of letters: {len('Hello')}")
```

## 💡 Tips and Best Practices

1. **Type Checking**: Use `type()` to check data types when debugging
2. **Input Validation**: Always convert `input()` to the appropriate type
3. **F-strings**: Use f-strings for cleaner string formatting
4. **Rounding**: Use `round()` for currency calculations
5. **Order of Operations**: Use parentheses to make calculations clear

## 🏆 Challenges

Try these additional challenges to reinforce your learning:

1. **Easy**: Create a BMI calculator that takes height and weight
2. **Medium**: Build a compound interest calculator
3. **Hard**: Create a unit converter (temperature, distance, weight)
4. **Expert**: Build a mortgage payment calculator

## 🔍 Common Mistakes to Avoid

1. **Forgetting Type Conversion**: `input()` always returns a string
2. **Integer vs Float Division**: `/` always returns float, `//` returns integer
3. **String Concatenation**: Can't directly add strings and numbers
4. **Precision Issues**: Floating-point arithmetic can be imprecise

## 📖 Key Functions and Methods

### Type Functions:
- `type(variable)` - Check the data type
- `int(value)` - Convert to integer
- `float(value)` - Convert to float
- `str(value)` - Convert to string

### Math Functions:
- `round(number, digits)` - Round to specified decimal places
- `abs(number)` - Absolute value
- `len(string)` - Length of string

### String Methods:
- `string[index]` - Access character at index
- `len(string)` - Get string length

## 🎓 What You've Learned

Day 2 builds essential skills for working with data in Python:

### Technical Skills:
- Data type identification and conversion
- Mathematical operations and order of operations
- String formatting and manipulation
- Error handling and debugging

### Problem-Solving Skills:
- Breaking down real-world problems (tip calculation)
- Handling user input validation
- Formatting output for readability
- Planning program logic step by step

**Next**: [Day 3 - Control Flow and Logical Operators](../Day%203/)

---

**💰 Sample Tip Calculator Logic:**
```
1. Get total bill amount
2. Get tip percentage choice
3. Get number of people
4. Calculate tip amount
5. Calculate total with tip
6. Divide by number of people
7. Format and display result
```

*Happy Calculating! 💰*
