# Hangman Game 🎯

A classic word-guessing game implemented in Python with ASCII art and interactive gameplay.

## 📖 Project Description

This is the **Day 7** project from the 100 Days of Code Python Bootcamp. The Hangman game challenges players to guess a hidden word letter by letter, with only 6 incorrect guesses allowed before losing the game.

## 🎮 How to Play

1. The game randomly selects a word from a predefined word list
2. You see blank spaces representing each letter in the word
3. Guess letters one at a time
4. Correct guesses reveal the letter's position(s) in the word
5. Incorrect guesses cost you a life (you start with 6 lives)
6. Win by guessing all letters before running out of lives
7. Lose if you make 6 incorrect guesses

## 🚀 How to Run

```bash
# Navigate to the project directory
cd "100 Days of Code - The Complete Python Pro Bootcamp/Day 7/task"

# Run the game
python main.py
```

## 📁 Project Files

- **`main.py`** - Main game logic and user interaction
- **`hangman_words.py`** - Contains the list of words for the game
- **`hangman_art.py`** - ASCII art for the hangman stages and logo
- **`solution.py`** - Complete solution reference

## 🎨 Features

- **ASCII Art**: Beautiful hangman drawings that update with each wrong guess
- **Word Validation**: Prevents duplicate letter guesses
- **Life Counter**: Visual display of remaining lives
- **Random Word Selection**: Different word each game
- **Input Validation**: Handles user input gracefully

## 🧠 Programming Concepts Demonstrated

- **Lists and Random Selection**: Using `random.choice()` to select words
- **String Manipulation**: Working with individual characters
- **Loops**: `while` loops for game continuation, `for` loops for string iteration
- **Conditional Logic**: Complex if/elif/else statements
- **Modular Programming**: Separating concerns across multiple files
- **ASCII Art Integration**: Importing and displaying visual elements

## 🎯 Game Flow

```
1. Display hangman logo
2. Select random word from word list
3. Create placeholder with underscores
4. Start game loop:
   - Show current word state
   - Display remaining lives
   - Get user guess
   - Check if letter already guessed
   - Update word display or reduce lives
   - Show hangman stage
   - Check win/lose conditions
5. Display final result
```

## 📝 Sample Gameplay

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
Guess a letter: a

Word to guess: _ a _ _ _ _

****************************6/6 LIVES LEFT****************************
Guess a letter: z

You have guessed a wrong letter z. You lose a life

  +---+
  |   |
  O   |
      |
      |
      |
=========

Word to guess: _ a _ _ _ _
```

## 🔧 Customization

You can easily customize the game by:

1. **Adding more words**: Edit `hangman_words.py` to include more words
2. **Changing difficulty**: Add longer or shorter words
3. **Modifying lives**: Change the starting number of lives in `main.py`
4. **Custom ASCII art**: Update `hangman_art.py` with your own drawings

## 🎓 Learning Outcomes

After completing this project, you'll understand:

- How to structure a complete Python program across multiple files
- Working with lists and random selection
- String manipulation and character-by-character processing
- Game loop implementation
- User input validation and error handling
- Importing and using custom modules

## 🏆 Challenges

Try these extensions to enhance your learning:

1. **Easy**: Add a hint system that reveals the word category
2. **Medium**: Implement difficulty levels with different word lengths
3. **Hard**: Add a scoring system based on word difficulty and remaining lives
4. **Expert**: Create a two-player mode where one player enters the word

---

**Part of the 100 Days of Code - Python Bootcamp by Angela Yu**

*Happy Coding! 🐍*
