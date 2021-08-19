import random
print("Welcome to random Coin Toss!")
while True:
    print("1-->Toss a Coin.         2-->Exit.")
    user=int(input("What do you want to do?"))
    if(user==1):
        number=random.randint(1,2)
        if(number==1):
            print("Heads")
        else:
            print("Tails")
    else:
        break
