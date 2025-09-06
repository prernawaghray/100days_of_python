# Day 14: Higher Lower Game 📊

Day 14 challenges you to build the Higher Lower Game, where players guess which option has more followers/likes/views. This project combines data handling, game logic, and user interaction.

## 📚 Topics Covered

### 1. Working with Data
- Handling structured data in Python
- Working with lists of dictionaries
- Accessing nested data structures
- Managing game data and state

### 2. Game Logic Implementation
- Comparing data values
- Tracking game progress and scores
- Managing game state and flow
- Implementing win/lose conditions

### 3. User Interface Design
- Creating engaging game presentations
- Formatting output for readability
- Handling user input and choices
- Providing clear feedback and instructions

### 4. Random Selection and Comparison
- Randomly selecting items from datasets
- Ensuring fair game mechanics
- Avoiding duplicate selections
- Implementing comparison logic

## 🗂️ Project Structure

### Main Project:
📊 **[Higher or Lower Project](./Higher%20or%20Lower%20Project/)** - Complete implementation of the popular social media comparison game

## 🎮 Higher Lower Game Project

The Day 14 capstone project is a Higher Lower game that:
- Uses real data about celebrities, brands, or social media accounts
- Randomly selects two options for comparison
- Asks players to guess which has more followers/likes/views
- Tracks consecutive correct guesses as score
- Ends game when player makes incorrect guess

### Game Features:
- **Real Data**: Uses actual follower counts, views, or other metrics
- **Random Selection**: Ensures different combinations each game
- **Score Tracking**: Counts consecutive correct guesses
- **Clear Presentation**: Formatted output with ASCII art
- **Immediate Feedback**: Shows correct answer after each guess
- **Replayability**: Different combinations make each game unique

### Sample Game Flow:
```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ /_/_/\__, /_/ /_/\___/_/     
        /____/                   
    __                           
   / /   ____ _      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

    _    __    
   | |  / /____
   | | / / ___/
   | |/ (__  ) 
   |___/____(_)

Against B: Ariana Grande, a Musician and actress, from United States.

Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1.

Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

    _    __    
   | |  / /____
   | | / / ___/
   | |/ (__  ) 
   |___/____(_)

Against B: Kim Kardashian, a Reality TV personality and businesswoman, from United States.

Who has more followers? Type 'A' or 'B': B
Sorry, that's wrong. Final score: 1
```

## 🧠 Key Programming Concepts

### Data Structure Management
```python
# Sample data structure
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    # More data entries...
]
```

### Random Selection Logic
```python
import random

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
```

### Game Flow Management
```python
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
```

### Data Formatting
```python
def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
```

## 🎯 Learning Objectives

By the end of Day 14, you should be able to:
- ✅ Work with complex data structures (lists of dictionaries)
- ✅ Implement random selection algorithms
- ✅ Create engaging game interfaces
- ✅ Handle game state and flow management
- ✅ Format and present data attractively
- ✅ Implement comparison and scoring logic
- ✅ Build complete interactive applications
- ✅ Apply all previous concepts in a cohesive project

## 🔧 Advanced Programming Concepts

### Data Validation and Edge Cases
```python
def ensure_different_accounts(account_a, account_b):
    """Ensure we don't compare the same account twice"""
    while account_a == account_b:
        account_b = get_random_account()
    return account_b

def validate_user_input(guess):
    """Validate and normalize user input"""
    guess = guess.lower().strip()
    if guess not in ['a', 'b']:
        print("Invalid input. Please enter 'A' or 'B'.")
        return None
    return guess
```

### Screen Management
```python
import os

def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game_state(account_a, account_b, score):
    """Display current game state"""
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
```

### Score and Statistics Tracking
```python
def track_high_score(current_score):
    """Track and update high score"""
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    
    if current_score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(current_score))
        print(f"New high score: {current_score}!")
    else:
        print(f"High score: {high_score}")
```

## 💡 Tips and Best Practices

1. **Data Organization**: Keep data in separate files for easy management
2. **Function Separation**: Break game logic into small, focused functions
3. **User Experience**: Provide clear instructions and feedback
4. **Error Handling**: Handle invalid inputs gracefully
5. **Code Reusability**: Write functions that can be easily modified

## 🏆 Challenges and Extensions

Try these enhancements to improve your game:

1. **Easy**: Add more data entries for variety
2. **Medium**: Implement different categories (sports, movies, brands)
3. **Hard**: Add difficulty levels with different data sets
4. **Expert**: Create a web version with images and better UI

## 🔍 Common Implementation Challenges

1. **Duplicate Selection**: Ensuring the same account isn't compared to itself
2. **Data Access**: Correctly accessing nested dictionary values
3. **Game Flow**: Managing when to continue vs end the game
4. **Score Persistence**: Keeping track of consecutive correct answers
5. **User Input**: Handling case sensitivity and invalid inputs

## 📖 Key Development Concepts

### Game Development Patterns:
- **Game Loop**: Main loop that continues until game over
- **State Management**: Tracking score, current accounts, game status
- **Random Events**: Using randomization for replayability
- **User Interaction**: Getting and validating user input

### Data Management:
- **Structured Data**: Using dictionaries for complex objects
- **Data Access**: Safely accessing nested data structures
- **Data Presentation**: Formatting data for user display
- **Data Validation**: Ensuring data integrity

## 🎓 What You've Accomplished

Day 14 represents another major milestone:

### Technical Mastery:
- Complex data structure manipulation
- Game logic implementation
- User interface design
- Random selection algorithms

### Problem-Solving Growth:
- Breaking down complex requirements
- Handling edge cases and validation
- Creating engaging user experiences
- Integrating multiple programming concepts

### Project Development Skills:
- Planning and implementing complete applications
- Code organization and structure
- Testing and debugging complex interactions
- Creating replayable and engaging software

**Next**: [Day 15 - Coffee Machine Project](../Day%2015/)

---

**📊 Higher Lower Game Architecture:**
```
Data Layer: List of dictionaries with account information
Game Logic: Random selection, comparison, scoring
User Interface: Display formatting, input handling
Game Flow: Loop management, state tracking
```

*Compare Your Way to Victory! 📊*
