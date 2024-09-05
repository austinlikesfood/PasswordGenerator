'''
Austin Kuykendall uploaded September 5, 2024
'''
import random

Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y",
           "x", "z"]
Special_Characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_"]
Numbers = ["0", "1", "2", "3", "4", "5","6", "7", "8", "9", "10"]

# you can do this two ways, have the user specify the amount of desired
# characters. Or you can use the randomizer function
lettersInput = int(input("how many letters would you like?\n"))
Special_CharactersInput = int(input("how many special characters? would you like?\n"))
numbersInput = int(input("how many numbers would you like?\n"))
# you can use the shuffle function after you put t back into the list.
password = []
for  char in range(0, lettersInput):
    password.append(random.choice(Letters))
for  char in range(0, Special_CharactersInput ):
    password.append(random.choice(Special_Characters))
for  char in range(0, numbersInput ):
    password.append(random.choice(Numbers))
print(password)
random.shuffle(password)
print (password)

passwordViewer = ""

for char in password:
    passwordViewer += char
print(f"Your password is: {passwordViewer}")