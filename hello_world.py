num = 100
for i in range(num):
    hello = i % 3
    world = i % 7

    if hello == 0:
        print ("Hello")
    elif world == 0:
        print ("World")
    else:
        print (i)
