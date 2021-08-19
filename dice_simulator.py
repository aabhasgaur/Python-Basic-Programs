import random
print("Welcome to the Dice Simulator!")
while True:
    print("1-->Roll a Dice.         2-->Exit.")
    user=int(input("What do you want to do?"))
    if(user==1):
        number=random.randint(1,6)
        print(number)
    else:
        break
