print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
cost = 0

if size == "S":
    cost = 15
    if pepperoni == "Y":
        cost += 2
elif size == "M":
    cost = 20
    if pepperoni == "Y":
        cost += 3
elif size == "L":
    cost = 25
    if pepperoni == "Y":
        cost += 3
else:
    print("You typed a wrong input!")
if extra_cheese == "Y":
    cost += 1
print(f"Your final bill is: ${cost}.")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed a wrong input!")
# if pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#       bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")