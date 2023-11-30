from random import randint
gussnumber=int(input("enter a number from 1 to 10"))
randomNumber=randint(1,10)
if gussnumber==randomNumber:
    print("you have won the game")
else:
    print("you have lost the game")
    print("randomnumber is",randomNumber)