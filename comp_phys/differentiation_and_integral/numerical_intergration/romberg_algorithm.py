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
def Romberg(y,a,b,eps=1e-6):
    T=[];S=[];C=[];R=[]
    T.append(T_integrate(y,a,b))
    n=1;m=0;ep=1
    while (ep>eps):
        m=m+1
        n=2*n
        h=(b-a)/n
        t=T[-1]/2
        for i in range(n):
            x=a+(i+1/2)*h
            t=t+h*y(x)/2
        T.append(t)
        if m>=1:
            S.append((4*T[-1]-T[-2])/3)
        if m>=2:
            C.append((16*S[-1]-S[-2])/15)
        if m>=3:
            R.append((64*C[-1]-C[-2])/63)
        if m>=4:
            ep=abs(R[-1]-R[-2])   
    return R[-1]
print(Romberg(y,a=0,b=10))

    
    