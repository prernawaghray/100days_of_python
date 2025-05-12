import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = ["rock", "paper", "scissors"]
# Get the user's choice
user_choice = input("Please enter your choice: \'rock\', \'paper\' or \'scissors\': ").lower()
if user_choice == "rock":
    print("Rock\n", rock)
elif user_choice == "paper":
    print("Paper \n", paper)
elif user_choice == "scissors":
    print("Scissors\n", scissors)
else:
    print("Incorrect input! Game over!")

# Make computer's choice
computers_choice = random.choice(game)

print(f"Computer's choice: \n")
if computers_choice == "rock":
    print("Rock\n", rock)
elif computers_choice == "paper":
    print("Paper \n", paper)
elif computers_choice == "scissors":
    print("Scissors\n", scissors)

'''
rock paper scissors rules:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
# rock = 0
# paper = 1
# scissors = 2

if user_choice == computers_choice:
    print("It's a tie!")
elif user_choice == "rock" and computers_choice == "scissors":
    print("You win!")
elif user_choice == "scissors" and computers_choice == "paper":
    print("You win!")
elif user_choice == "paper" and computers_choice == "rock":
    print("You win!")
else:
    print("You lose!")

