import math
def y(x):
    if x==0:
        y=1
    else:
        y=math.sin(x)/x
    return y
def T_integrate(y,a,b):
    T=1/2*(b-a)*(y(b)+y(a))
    return T
def Variable_T_integrate(y,a,b,eps=1e-6):
    n=1;ep=1
    T=T_integrate(y,a,b)
    while (ep>eps):
        n=2*n
        h=(b-a)/n  
        T_new=T/2                                
        for i in range(n):
            x=a+(i+1/2)*h
            T_new=T_new+h*y(x)/2
        ep=abs(T-T_new)
        T=T_new
    return T
a=0;b=10
print(Variable_T_integrate(y,a,b))

        


