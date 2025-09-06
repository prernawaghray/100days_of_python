# Day 1: Working with Variables in Python to Manage Data 🐍

Welcome to Day 1 of the 100 Days of Code Python Bootcamp! This day introduces the fundamental concepts of Python programming.

## 📚 Topics Covered

### 1. Printing to the Console
- Using the `print()` function
- Displaying text and messages
- Basic output formatting

### 2. String Manipulation
- Working with text strings
- String concatenation
- Using quotes in strings

### 3. Input from Users
- Getting user input with `input()`
- Storing user responses
- Interactive programs

### 4. Variables
- Creating and naming variables
- Storing different types of data
- Variable assignment and reassignment

### 5. Variable Naming Conventions
- Python naming rules
- Best practices for variable names
- Avoiding reserved keywords

## 🗂️ Exercises and Projects

### Practice Exercises:
1. **[Printing](./Printing/)** - Learn to use the print function
2. **[String Manipulation](./String%20Manipulation/)** - Work with text strings
3. **[Inputs](./Inputs/)** - Get input from users
4. **[Variables](./Variables/)** - Store and use data
5. **[Variable Naming](./Variable%20Naming/)** - Proper naming conventions

### Main Project:
🎯 **[Band Name Generator](./Band%20Name%20Generator%20Project/)** - Create a program that generates band names based on user input

## 🎮 Band Name Generator Project

The capstone project for Day 1 is a Band Name Generator that:
- Greets the user
- Asks for the city they grew up in
- Asks for a pet's name
- Combines both to create a unique band name

### How to Run:
```bash
cd "Day 1/Band Name Generator Project"
python main.py
```

### Sample Output:
```
Welcome to the Band Name Generator.
What's name of the city you grew up in?
> Austin
What's your pet's name?
> Buddy
Your band name could be Austin Buddy
```

## 🧠 Key Programming Concepts

### Variables
```python
# Creating variables
name = "Angela"
age = 25
height = 5.6

# Using variables
print("My name is " + name)
print("I am " + str(age) + " years old")
```

### String Concatenation
```python
# Combining strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

### User Input
```python
# Getting input from user
user_name = input("What is your name? ")
print("Hello " + user_name)
```

## 🎯 Learning Objectives

By the end of Day 1, you should be able to:
- ✅ Use the `print()` function to display output
- ✅ Work with strings and perform basic string operations
- ✅ Get input from users using `input()`
- ✅ Create and use variables to store data
- ✅ Follow Python naming conventions for variables
- ✅ Build a simple interactive program

## 🔧 Python Concepts Introduced

- **`print()` function**: Display output to console
- **Strings**: Text data enclosed in quotes
- **`input()` function**: Get user input
- **Variables**: Named storage for data
- **String concatenation**: Combining strings with `+`
- **Comments**: Using `#` for code documentation

## 💡 Tips and Best Practices

1. **Variable Naming**: Use descriptive names like `user_name` instead of `x`
2. **String Quotes**: Use consistent quote style (single or double)
3. **Comments**: Add comments to explain your code
4. **Testing**: Test your programs with different inputs
5. **Debugging**: Use `print()` statements to check variable values

## 🏆 Challenges

Try these additional challenges to reinforce your learning:

1. **Easy**: Create a program that asks for your favorite color and food, then creates a superhero name
2. **Medium**: Build a Mad Libs generator that asks for different types of words
3. **Hard**: Create a program that calculates and displays your age in days

## 📖 Additional Resources

- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [PEP 8 - Python Style Guide](https://pep8.org/)

---

**Next**: [Day 2 - Understanding Data Types and How to Manipulate Strings](../Day%202/)

*Happy Coding! 🚀*
