import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy version

chosen_letters = ""
for i in range(0, nr_letters):
    chosen_letters += random.choice(letters)

chosen_numbers = ""
for i in range(0, nr_numbers):
    chosen_numbers += random.choice(numbers)

chosen_symbols = ""
for i in range(0, nr_symbols):
    chosen_symbols += random.choice(symbols)
final_password_easy = chosen_letters + chosen_numbers + chosen_symbols

print("Easy version - Your chosen password is: ", final_password_easy)

# hard version

# the following method works if you are building from scratch
# but if you are building on top of the previous solution then
# just take the final password, convert to list, shuffle it and
# finally convert back to string
#
# chosen_letters = []
# for i in range(0, nr_letters):
#     chosen_letters.append(random.choice(letters))
#
# chosen_numbers = []
# for i in range(0, nr_numbers):
#     chosen_numbers.append(random.choice(numbers))
#
# chosen_symbols = []
# for i in range(0, nr_symbols):
#     chosen_symbols.append(random.choice(symbols))
#
# pwd_list = chosen_letters + chosen_numbers + chosen_symbols

pwd_list = list(final_password_easy)
random.shuffle(pwd_list)
final_password_hard = "".join(pwd_list)
print("Hard version - Your chosen password is: ", final_password_hard)

