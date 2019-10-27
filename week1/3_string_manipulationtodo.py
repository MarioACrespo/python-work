"""
Personality questionnaire
"""

# TODO: ask a user to input their full name in lower case lettters
#First_nam = input("Hello, what is your full name in lowercase?")
#print(First_nam)
# TODO: write a program that asks a user 6 unique questions about them and see if it works!
height = input("How tall are you?")
name = input("What is your name?").title()
pet = input("What was your first pet's name?").title()
age = input("How old are you?")
bday = input("when is your birthday?")
family = input("How many sibings do you have?")

print(name + height + pet + family + age + bday)
# TODO: use input functions however you would like
print("Hi, I am" + name + " and I am" + height).title()
print("I have" + family + " sibings, and my birthday is on" + bday)
print("I am" + age + " years old and my pets name is" + pet).title()
# TODO: print out the results in a neat format and make sure to capitalize the user's name with the
print("Hi, I am mario  and I am 5ft")
print("I have 2  sibings, and my birthday is on may 18")
print("I am 15  years old and my pets name is goldy")

# TODO: title function
#name = input("What is your name?").title()
#pet = input("What was your first pet's name?").title()