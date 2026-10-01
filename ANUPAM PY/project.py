import time
print("Rectangle Calculation Software")
print("")
x = input("Kindy provide LENGTH |")
y = input("Breath|")
x = int(x)
y = int(y)
area = y*x
perimeter = 2*(x+y)
tick = "calcutating..."
print(tick)
time.sleep(1)
print("\033c", end="") 
print("Your area has been calculated as" )
print(area)
print("Your perimeter has been calculated as")
print(perimeter)











