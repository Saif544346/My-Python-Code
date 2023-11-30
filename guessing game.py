from random import randint
for x in range(1,6):
  guessnumber=int(input("Enter a number from 1 to 5:"))
  randomnumber=randint(1,5)
  if guessnumber==randomnumber:
    print("you have won")
  else:
    print("lost")
    print(randomnumber)