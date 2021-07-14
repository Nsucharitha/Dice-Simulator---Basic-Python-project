import random
#Dice simulator - basic program
key = 'y'
while (key == 'y'):
    #randomly generate a number between 1 to 6
    x = random.randint(1, 6)
    if x == 1:
        print("---------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("----------")
    if x == 2:
        print("---------")
        print("|    0   |")
        print("|        |")
        print("|    0   |")
        print("----------")
    if x == 3:
        print("---------")
        print("| 0      |")
        print("|   0    |")
        print("|      0 |")
        print("----------")
    if x == 4:
        print("---------")
        print("| 0    0  |")
        print("|         |")
        print("| 0    0  |")
        print("----------")
    if x == 5:
        print("---------")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")
    if x == 6:
        print("---------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")
    #To roll the dice again
    print("To continue press 'y'")
    key = input()
