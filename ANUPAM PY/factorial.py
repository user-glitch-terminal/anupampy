def factorial(number):
    result = 1
 
    for i in range(1, number+1):
        result = result * i
    return result
while True:
    x = int(input("Enter to get factorial: "))
    x = factorial(x)
    print(x)