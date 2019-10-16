#local and global variable

z = 10

def func1():
    global z
    print ("Global: ",z)
    z = 3
    print ("New value of z:",z)

def func2(x,y):
    global z
    return x+y+z

func1()
total = func2(4,5)
print ("total:", total)
