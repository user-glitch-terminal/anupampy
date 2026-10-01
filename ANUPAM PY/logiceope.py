#write a program to check whether the number is positive negative or zero

try:
    num = input("ENter any positive negative or zero number:  ")
    if num == 0:
        print("The number is zero")

    elif num < 0:
        print("NUmber is negative")

    else:
        print("The number is positive")

except:
    print("Error")
