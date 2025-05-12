print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_lr = input("Where would you like to go? Type \'Left\' or \'Right\' ")
if choice_lr.lower() == "left":
    print("Well done! You have encountered a lake. Would you like to wait for a boat or swim over?")
    choice_lake = input("Type \'Swim\' or \'Wait\' ")
    if choice_lake.lower() == "wait":
        print("Well done! Now you have come across 3 doors. Which one would you like to choose?")
        choice_door = input("Type \'Red\', \'Blue\' or \'Yellow\' to choose ")
        if choice_door.lower() == "yellow":
            print("Congratulations! You won!")
        elif choice_door.lower() == "red":
            print("Sorry, you're toast, burnt by a fire! You lose!")
            exit()
        elif choice_door.lower() == "blue":
            print("Sorry, you're eaten by beasts! You lose!")
            exit()
        else:
            print("Sorry, incorrect option! You lose!")
            exit()
    elif choice_lake.lower() == "swim":
        print("Sorry, you've been attacked by trout! You lose!")
        exit()
    else:
        print("Sorry, incorrect option! You lose!")
        exit()
elif choice_lr.lower() == "right":
    print("Sorry, you fell into a hole! You lose!")
else:
    print("Incorrect option! Game over!")
