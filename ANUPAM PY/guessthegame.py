import random
while True:
    x = random.randint(1 ,10)
    y = input("Guess a number from 1 to 10 : ")
    while True:
        if y==x:
            print("U guessed the number")
            break
            continue

        else:
        
            print(f"sry the number was {x}  ")
            break
            continue
