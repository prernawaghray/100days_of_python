# Day 12: Scope & Number Guessing Game 🎯

Day 12 explores the concept of scope in Python and applies this knowledge to build a Number Guessing Game with different difficulty levels.

## 📚 Topics Covered

### 1. Namespaces and Scope
- Understanding local vs global scope
- How Python resolves variable names
- Scope hierarchy and variable lookup
- Best practices for variable scope

### 2. Block Scope
- Scope within if statements, loops, and functions
- How Python handles block-level variables
- Differences from other programming languages
- Variable lifetime and accessibility

### 3. Global Variables
- When and how to use global variables
- The `global` keyword
- Modifying global variables from functions
- Avoiding global variable pitfalls

### 4. Global Constants
- Creating and using constants in Python
- Naming conventions for constants
- When constants are appropriate
- Organizing constants in programs

## 🗂️ Exercises and Projects

### Practice Exercises:
1. **[Namespaces and Scope](./Namespaces%20and%20Scope/)** - Understanding variable scope rules
2. **[Block Scope](./Block%20Scope/)** - Scope within code blocks
3. **[Global Vars](./Global%20Vars/)** - Working with global variables
4. **[Global Constants](./Global%20Constants/)** - Using constants effectively

### Main Project:
🎯 **[Number Guessing Game](./Number%20Guessing%20Project/)** - Interactive guessing game with difficulty levels and attempt tracking

## 🎮 Number Guessing Game Project

The Day 12 capstone project is a number guessing game that:
- Generates a random number between 1 and 100
- Offers two difficulty levels (Easy: 10 attempts, Hard: 5 attempts)
- Tracks remaining attempts using global variables
- Provides feedback on guesses (too high/too low)
- Demonstrates practical scope management

### Game Features:
- **Random Number Generation**: Secret number between 1-100
- **Difficulty Levels**: Easy (10 attempts) or Hard (5 attempts)
- **Attempt Tracking**: Global variable manages remaining guesses
- **Feedback System**: Tells player if guess is too high or low
- **Win/Lose Conditions**: Clear game ending scenarios
- **Input Validation**: Handles invalid inputs gracefully

### Sample Game Flow:
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.

You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.

You have 8 attempts remaining to guess the number.
Make a guess: 37
You got it! The answer was 37.
```

## 🧠 Key Programming Concepts

### Local vs Global Scope
```python
# Global scope
enemies = 1

def increase_enemies():
    # Local scope - creates new local variable
    enemies = 2
    print(f"enemies inside function: {enemies}")  # 2

increase_enemies()
print(f"enemies outside function: {enemies}")  # 1 (unchanged)
```

### Using Global Keyword
```python
# Global variable
enemies = 1

def increase_enemies():
    global enemies  # Modify global variable
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()  # enemies becomes 2
print(f"enemies outside function: {enemies}")  # 2
```

### Scope Hierarchy
```python
# Global scope
x = "global"

def outer_function():
    # Enclosing scope
    x = "enclosing"
    
    def inner_function():
        # Local scope
        x = "local"
        print(x)  # Prints "local"
    
    inner_function()
    print(x)  # Prints "enclosing"

outer_function()
print(x)  # Prints "global"
```

### Constants Convention
```python
# Constants (by convention, all uppercase)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
```

## 🎯 Learning Objectives

By the end of Day 12, you should be able to:
- ✅ Understand local, global, and enclosing scope
- ✅ Use the `global` keyword appropriately
- ✅ Recognize when variables are in different scopes
- ✅ Apply scope concepts to manage game state
- ✅ Use constants to make code more maintainable
- ✅ Debug scope-related issues in your code
- ✅ Design programs with proper variable organization
- ✅ Build interactive games with state management

## 🔧 Python Scope Rules (LEGB)

### LEGB Rule - Python's Scope Resolution:
1. **L**ocal - Inside the current function
2. **E**nclosing - In any outer function
3. **G**lobal - At the module level
4. **B**uilt-in - In the built-in namespace

```python
# Built-in scope (print, len, etc.)
print("Hello")  # 'print' is in built-in scope

# Global scope
global_var = "I'm global"

def outer_function():
    # Enclosing scope
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local scope
        local_var = "I'm local"
        
        # Can access all scopes
        print(local_var)      # Local
        print(enclosing_var)  # Enclosing
        print(global_var)     # Global
        print(len("test"))    # Built-in
    
    inner_function()

outer_function()
```

### Scope Best Practices
```python
# Good: Use parameters instead of global variables
def calculate_total(price, tax_rate):
    return price * (1 + tax_rate)

# Avoid: Using global variables unnecessarily
total = 0  # Global variable
def bad_calculate_total(price):
    global total
    total = price * 1.08  # Modifies global state
```

## 💡 Tips and Best Practices

1. **Minimize Globals**: Use global variables sparingly
2. **Constants**: Use ALL_CAPS for constants
3. **Parameters**: Pass data through parameters when possible
4. **Clear Names**: Use descriptive variable names in all scopes
5. **Scope Planning**: Think about variable scope when designing functions

## 🏆 Challenges

Try these additional challenges to reinforce your learning:

1. **Easy**: Create a simple counter program using global variables
2. **Medium**: Build a multi-level game with different global settings
3. **Hard**: Create a program with nested functions that share variables
4. **Expert**: Design a configuration system using global constants

## 🔍 Common Scope Mistakes

1. **UnboundLocalError**: Trying to modify global variable without `global` keyword
2. **Shadowing**: Accidentally creating local variables with same name as globals
3. **Scope Confusion**: Not understanding which scope a variable belongs to
4. **Global Overuse**: Using global variables when parameters would be better
5. **Constant Modification**: Accidentally changing values meant to be constant

## 📖 Key Scope Concepts

### Variable Assignment Rules:
- Assignment creates local variables by default
- Use `global` keyword to modify global variables
- Reading variables follows LEGB rule
- Function parameters are always local

### Scope Keywords:
- `global` - Declare variable as global
- `nonlocal` - Access enclosing scope variable (advanced)

### Best Practices:
- Keep variables in the smallest scope possible
- Use constants for values that don't change
- Pass data through parameters rather than globals
- Use descriptive names to avoid confusion

## 🎓 What You've Learned

Day 12 introduces crucial programming concepts for larger applications:

### Technical Skills:
- Variable scope and namespace understanding
- Global variable management
- Constant usage and conventions
- State management in interactive programs

### Problem-Solving Skills:
- Organizing variables by scope and purpose
- Managing program state across functions
- Designing clean, maintainable code architecture
- Debugging scope-related issues

### Software Engineering Principles:
- Minimizing global state for better code quality
- Using constants for configuration values
- Proper variable organization and naming
- Code maintainability and readability

**Next**: [Day 13 - Debugging](../Day%2013/)

---

**🎯 Number Guessing Game Architecture:**
```
Global Constants: EASY_LEVEL_TURNS, HARD_LEVEL_TURNS
Global Variables: attempts (managed across functions)
Functions: check_answer(), set_difficulty(), game()
Game Loop: Continues until win or attempts exhausted
```

*Scope Your Way to Success! 🎯*
