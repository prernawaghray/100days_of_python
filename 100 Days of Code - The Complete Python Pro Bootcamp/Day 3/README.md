# Day 3: Control Flow and Logical Operators 🔀

Day 3 introduces conditional statements and logical operators, teaching you how to make your programs make decisions and follow different paths based on conditions.

## 📚 Topics Covered

### 1. If/Else Statements
- Basic conditional logic with `if` and `else`
- Making programs respond to different conditions
- Boolean expressions and comparisons
- Indentation and code blocks in Python

### 2. Nested If Statements and Elif
- Using `elif` for multiple conditions
- Nesting if statements inside other if statements
- Creating complex decision trees
- Best practices for readable conditional logic

### 3. Multiple If Statements
- When to use multiple separate `if` statements
- Difference between `elif` and multiple `if`s
- Independent vs dependent conditions
- Program flow control

### 4. Logical Operators
- `and` operator - both conditions must be True
- `or` operator - at least one condition must be True
- `not` operator - reverses the boolean value
- Combining multiple logical operators

### 5. Modulo Operator
- Using `%` to find remainders
- Checking for even/odd numbers
- Divisibility testing
- Practical applications in programming

## 🗂️ Exercises and Projects

### Practice Exercises:
1. **[If Else](./If%20Else/)** - Basic conditional statements
2. **[Nesting and Elif](./Nesting%20and%20Elif/)** - Complex decision making
3. **[Multiple Ifs](./Multiple%20Ifs/)** - Independent conditions
4. **[Logical Operators](./Logical%20Operators/)** - Combining conditions
5. **[Modulo](./Modulo/)** - Working with remainders
6. **[Python Pizza](./Python%20Pizza/)** - Pizza ordering system practice

### Main Project:
🏴‍☠️ **[Treasure Island Project](./Treasure%20Island%20Project/)** - Interactive adventure game with multiple paths and endings

## 🎮 Treasure Island Project

The Day 3 capstone project is an interactive text-based adventure game that:
- Presents the player with multiple choices
- Uses nested conditional statements to create different story paths
- Has multiple possible endings based on player decisions
- Demonstrates complex program flow and decision making

### Game Features:
- Multiple choice points that affect the story
- Different endings based on player choices
- ASCII art and engaging narrative
- Demonstrates all Day 3 concepts in action

### Sample Game Flow:
```
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad. Where do you want to go? 
  Type "left" or "right"
> left
You've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.
> wait
You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?
> yellow
You found the treasure! You Win!
```

## 🧠 Key Programming Concepts

### Basic If/Else Structure
```python
# Simple if/else
age = 18
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
```

### Elif for Multiple Conditions
```python
# Multiple conditions with elif
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Logical Operators
```python
# AND operator - both conditions must be True
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive!")

# OR operator - at least one condition must be True
day = "Saturday"
day2 = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# NOT operator - reverses boolean value
is_raining = False
if not is_raining:
    print("Let's go for a walk!")
```

### Modulo Operator Applications
```python
# Check if number is even or odd
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Check divisibility
year = 2024
if year % 4 == 0:
    print("Might be a leap year")
```

## 🎯 Learning Objectives

By the end of Day 3, you should be able to:
- ✅ Write conditional statements using if/else
- ✅ Use elif for multiple condition checking
- ✅ Understand when to use multiple if vs elif
- ✅ Combine conditions using logical operators (and, or, not)
- ✅ Use the modulo operator for mathematical checks
- ✅ Create nested conditional statements
- ✅ Build interactive programs with multiple decision points
- ✅ Design program flow with complex logic

## 🔧 Python Concepts Introduced

### Comparison Operators
```python
# Comparison operators return True or False
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True (equality)
print(5 != 3)   # True (not equal)
print(5 >= 5)   # True (greater than or equal)
print(5 <= 4)   # False (less than or equal)
```

### Boolean Values
```python
# Boolean variables
is_sunny = True
is_raining = False

# Boolean expressions
has_umbrella = True
should_go_out = is_sunny or (is_raining and has_umbrella)
```

### Nested Conditions
```python
# Nested if statements
weather = "sunny"
temperature = 75

if weather == "sunny":
    if temperature > 70:
        print("Perfect day for the beach!")
    else:
        print("Sunny but a bit cold")
else:
    print("Not a sunny day")
```

## 💡 Tips and Best Practices

1. **Indentation**: Python uses indentation to define code blocks - be consistent
2. **Logical Flow**: Plan your conditions from most specific to most general
3. **Readability**: Use parentheses to make complex logical expressions clear
4. **Testing**: Test all possible paths through your conditional statements
5. **Simplification**: Look for ways to simplify complex nested conditions

## 🏆 Challenges

Try these additional challenges to reinforce your learning:

1. **Easy**: Create a simple calculator that handles different operations
2. **Medium**: Build a grade calculator that considers multiple assignments
3. **Hard**: Create a text-based RPG battle system
4. **Expert**: Design a complex decision tree for a loan approval system

## 🔍 Common Mistakes to Avoid

1. **Indentation Errors**: Python is strict about indentation - use 4 spaces consistently
2. **Assignment vs Equality**: Use `==` for comparison, `=` for assignment
3. **Logical Operator Confusion**: Remember `and` requires both conditions to be True
4. **Missing Colons**: Don't forget the `:` after if, elif, and else statements
5. **Unreachable Code**: Make sure all conditions can be reached

## 📖 Key Operators and Keywords

### Conditional Keywords:
- `if` - Check a condition
- `elif` - Check additional conditions
- `else` - Default case when no conditions are met

### Comparison Operators:
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to

### Logical Operators:
- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Reverses the boolean value

### Mathematical Operators:
- `%` - Modulo (remainder after division)

## 🎓 What You've Learned

Day 3 introduces fundamental programming concepts that you'll use constantly:

### Technical Skills:
- Conditional logic and decision making
- Boolean expressions and logical operators
- Program flow control
- Complex nested conditions

### Problem-Solving Skills:
- Breaking down complex decisions into simple conditions
- Planning program flow and logic paths
- Creating interactive user experiences
- Handling multiple scenarios and edge cases

**Next**: [Day 4 - Randomization and Python Lists](../Day%204/)

---

**🏴‍☠️ Adventure Game Logic Flow:**
```
Start → Choice 1 → Choice 2 → Choice 3 → Ending
  ↓         ↓         ↓         ↓        ↓
Left/Right Wait/Swim Red/Yellow/Blue Win/Lose
```

*Choose Your Path Wisely! 🗺️*
