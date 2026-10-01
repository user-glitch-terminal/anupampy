import time
t = time.localtime()
td = time.strftime("%Y-%m-%d", t)
tt = int(time.strftime("%H", t))
ttt = time.strftime("%H:%M:%S", t)
def cc():
    if 5 < tt < 12:
        greeting = "Good Morning!"
    elif 12 < tt < 17:
        greeting = "Good Afternoon!"
    elif 17 < tt < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    return greeting
print(td)
print(ttt)
print(cc())

