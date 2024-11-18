import string
import random

s1 = list(string.ascii_lowercase)
s2 = list (string.ascii_uppercase)
s3 = list (string.digits)
s4 = list (string.punctuation)

input_lenght = input("How many characters do you want in your password? (min 8) \n\t")

try:
    character_number = int (input_lenght)
    if character_number < 8:
        print ("Your number should be at least 8 \n")
        input_lenght = input ("Please, Enter your number again (min 8): \n\t")
except:
    print("Please, enter numbers only.")
    input_lenght = input ("How many character do you want in your password? (min 8)")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

    random.shuffle(result)

password = "".join(result)
print("Strong password: ", password)