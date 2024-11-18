import string
import random

lenght = int(input("Enter password lenght: (Atleast 8 characters)\n\t"))

print ("Choose characters for you password:\n\t 1. Digits\n\t 2. Letters\n\t 3.Special characters\n\t 4.Exit")

characterList = ""

choice=int(input("Pick a number "))

if (choice == 1):
    characterList+= string.ascii_letters
elif (choice == 2):
    characterList += string.digits
elif (choice == 3):
    characterList += string.punctuation
else:
    print ("Please pick a valid option")

password = []

for i in range(lenght):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print ("The random password is " + "".join(password))