import time
while True:
    t = time.localtime()
    f = time.strftime("%H:%M:%S", t) 

    print(f)


