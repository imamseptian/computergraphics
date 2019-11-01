import matplotlib.pyplot as plt
import time

def bresenham(x0,y0,x1,y1):
    t1=time.time()
    dx = x1-x0
    dy = y1-y0
    dx2=int(2*abs(dx))
    dy2=int(2*abs(dy))
    m=dy/dx
    x=[]
    y=[]
    x.append(x0)
    y.append(y0)
    c=0
    if(m>0 and m<1):
        pk = dy2 - abs(dx)
        while(x[c]<x1):
            c=c+1
            if(pk>=0):
                x.append(x[c-1]+1)
                y.append(y[c-1]+1)
            else:
                x.append(x[c - 1] + 1)
                y.append(y[c - 1])
            pk=pk+dy2-dx2*(y[c]-y[c-1])
    elif(m>=1):
        pk = dx2 - abs(dy)
        while (y[c]<y1):
            c = c + 1
            if (pk >= 0):
                x.append(x[c - 1] + 1)
                y.append(y[c - 1] + 1)
            else:
                x.append(x[c - 1])
                y.append(y[c - 1] + 1)
            pk = pk + dx2 - dy2 * (x[c] - x[c - 1])
    elif(m>-1 and m<0):
        pk = dy2 - abs(dx)
        while(x[c]<x1):
            c=c+1
            if(pk>=0):
                x.append(x[c-1]+1)
                y.append(y[c-1]-1)
            else:
                x.append(x[c - 1] + 1)
                y.append(y[c - 1])
            pk=pk+dy2-dx2*(y[c-1]-y[c])
    else:
        pk = dx2 - abs(dy)
        while (y[c] < y1):
            c = c + 1
            if (pk >= 0):
                x.append(x[c - 1] - 1)
                y.append(y[c - 1] + 1)
            else:
                x.append(x[c - 1])
                y.append(y[c - 1] + 1)
            pk = pk + dx2 - dy2 * (x[c-1]-x[c])

    t2=time.time()
    print("Execution Time : ",(t2-t1),"s")
    plt.plot(x,y)
    plt.show()


bresenham(2,1,100,1000)








