import matplotlib.pyplot as plt
import time

def dda(x0,y0,x1,y1):
    t1=time.time()
    dx = (x1 - x0)
    dy = (y1 - y0)
    m = dy / dx
    x = []
    y = []
    x.append(x0)
    y.append(y0)
    step = 0
    if(abs(dy)>abs(dx)):
        step = abs(dy)
    else:
        step = abs(dx)
    xinc = dx/step
    yinc = dy/step
    c=0
    xa = x0
    ya = y0
    if(step==abs(dy)):
        while(y[c]<y1):
            c=c+1
            xa = xa + xinc
            ya = ya + yinc
            x.append(round(xa))
            y.append(round(ya))
    else:
        while(x[c]<x1):
            c=c+1
            xa = xa + xinc
            ya = ya + yinc
            x.append(round(xa))
            y.append(round(ya))

    t2=time.time()
    print("Execution Time : ",(t2-t1),"s")
    plt.plot(x, y)
    plt.show()
    

dda(7,12,4,20)

