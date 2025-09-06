# Day 7: Hangman Project 🎯

Day 7 is all about building the classic Hangman game! This project brings together everything learned in the first 6 days to create a complete, interactive game.

## 📚 Topics Covered

### Core Concepts Applied:
- **Lists and Random Selection**: Choosing words from a word list
- **String Manipulation**: Working with individual characters
- **Loops**: `while` loops for game continuation, `for` loops for iteration
- **Conditional Logic**: Complex if/elif/else statements
- **Functions**: Organizing code into reusable functions
- **Modular Programming**: Separating code across multiple files

## 🎮 The Hangman Game

### Game Rules:
1. A random word is selected from a word list
2. Player sees blank spaces representing each letter
3. Player guesses letters one at a time
4. Correct guesses reveal letter positions
5. Wrong guesses add to the hangman drawing
6. Player wins by guessing all letters
7. Player loses after 6 wrong guesses

### Game Features:
- 🎨 **ASCII Art**: Beautiful hangman drawings and logo
- 🔄 **Input Validation**: Prevents duplicate guesses
- 📊 **Life Counter**: Visual display of remaining attempts
- 🎲 **Random Words**: Different word each game
- 🏆 **Win/Lose Conditions**: Clear game endings

## 🗂️ Project Structure

### Step-by-Step Development:
1. **[Step 1](./Step%201/)** - Basic word guessing setup
2. **[Step 2](./Step%202/)** - Replace blanks with correct guesses
3. **[Step 3](./Step%203/)** - Check win condition
4. **[Step 4](./Step%204/)** - Track wrong guesses and lives
5. **[Step 5](./Step%205/)** - Complete game with ASCII art

### Final Project:
🎯 **[Complete Hangman Game](./task/)** - Fully functional game with all features

## 🚀 How to Play

```bash
# Navigate to the completed game
cd "Day 7/task"

# Run the hangman game
python main.py
```

## 📁 Game Files

- **`main.py`** - Main game logic and flow
- **`hangman_words.py`** - List of words for the game
- **`hangman_art.py`** - ASCII art for hangman stages and logo
- **`solution.py`** - Complete reference solution

## 🧠 Key Programming Concepts

### Random Word Selection
```python
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
```

### Character-by-Character Processing
```python
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

### Game State Management
```python
lives = 6
game_over = False
correct_letters = []

while not game_over:
    # Game logic here
    if lives == 0:
        game_over = True
    if "_" not in display:
        game_over = True
```

## 🎨 ASCII Art Integration

The game includes beautiful ASCII art:
- **Hangman Logo**: Displayed at game start
- **Hangman Stages**: 7 different drawings showing game progress
- **Visual Feedback**: Clear representation of remaining lives

## 🎯 Learning Objectives

By completing Day 7, you should be able to:
- ✅ Build a complete interactive game
- ✅ Use loops effectively for game flow
- ✅ Implement complex conditional logic
- ✅ Work with multiple Python files
- ✅ Handle user input validation
- ✅ Create engaging user experiences
- ✅ Debug and test complete programs

## 🏆 Programming Skills Developed

### Problem Solving:
- Breaking down complex problems into steps
- Planning program flow and logic
- Debugging multi-file programs

### Code Organization:
- Separating concerns across files
- Using meaningful variable names
- Writing clean, readable code

### User Experience:
- Creating engaging interfaces
- Providing clear feedback
- Handling edge cases gracefully

## 💡 Code Highlights

### Duplicate Guess Prevention:
```python
if guess in correct_letters:
    print(f"You have already guessed {guess}")
```

### Dynamic Word Display:
```python
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

### Life Management:
```python
if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    
    if lives == 0:
        game_over = True
        print(f"***********************YOU LOSE**********************")
        print(f"The word was {chosen_word}")
```

## 🔧 Customization Ideas

Enhance your hangman game with these features:

1. **Easy**: Add word categories and hints
2. **Medium**: Implement difficulty levels
3. **Hard**: Add a scoring system
4. **Expert**: Create multiplayer functionality

## 🎓 What's Next?

Day 7 marks the completion of the beginner fundamentals! You've now learned:
- Variables and data types
- Control flow and loops
- Functions and modular programming
- Complete project development

**Next**: [Day 8 - Function Parameters & Caesar Cipher](../Day%208/)

---

**🎮 Game Sample:**
```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _ _ _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: 
```

*Happy Gaming! 🎯*
