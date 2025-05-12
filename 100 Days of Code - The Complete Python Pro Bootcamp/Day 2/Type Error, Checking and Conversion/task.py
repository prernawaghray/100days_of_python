print(len("12345"))
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

print("123"+"456")
print(int("123")+int("456"))

print(str(123)+str(456))
print(float(123)+float(456))
print(bool(123)+bool(456))

#print("Number of letters in your name: " + len(input("Enter your name")))

name_of_the_user = input("Enter your name") #str
length_of_name = len(name_of_the_user) #int
print("Number of letters in your name: " +str(length_of_name))