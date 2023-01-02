import sys
def onlinestats(n,x):
    global m,var,x_0
    if x < 0:
        sys.exit()
    if n == 1:
        print("Mean is {} variance is {}".format(x,0))
        n+=1
        x_0=x
    elif n == 2:
        m = float((x+x_0) / 2)
        var = (x_0 - m) ** 2 + (x - m) ** 2
        print("Mean is {} variance is {}".format(m,var))
        n+=1
    else:
        mean1 = m + (x - m) / n
        var1 = ((n - 2) / (n - 1)) * var + (x - m) ** 2 / n
        print("Mean is {} variance is {}".format(mean1, var1))
        m = mean1
        var = var1
        n+=1
    x = float(input("Enter a number     "))
    onlinestats(n,x)
y=float(input("Enter a number      "))
n=1
onlinestats(n,y)
