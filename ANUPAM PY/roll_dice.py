import random
while True:
    
    print("Do you want to roll the dice 'y/n' : ")
    x = input()
    if x == "y":
        y = random.randint(1,6 )
        print(y)

    elif x=="n":
        print("OKay, Have a good day")
        break

    else:
        print("Enter y/n only")
