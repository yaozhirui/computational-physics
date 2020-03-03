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
def S_integrate(y,a,b):
    S=1/6*(b-a)*(y(a)+y(b)+4*y((a+b)/2))
    return S
def C_integrate(y,a,b):
    h=(b-a)/4
    C=(b-a)*(7/90*(y(a)+y(b))+16/45*(y(a+h)+y(a+3*h))+2/15*y(a+2*h))
    return C
def complex_T(y,a,b):
    T=0
    for i in range(n):
        x=a+i*h
        T=T+T_integrate(y,x,x+h)
    return T
def complex_S(y,a,b):
    S=0
    for i in range(int(n/2)):
        x=a+2*i*h
        S=S+S_integrate(y,x,x+2*h)
    return S
def complex_C(y,a,b):
    C=0
    for i in range(int(n/4)):
        x=a+4*i*h
        C=C+C_integrate(y,x,x+4*h)
    return C 
str1=""
for i in [1,2,3,4,6,8,10]:
    n=2**i
    h=(b-a)/n
    str1=str1+str("%.3e"%h)+" "+"&"+" "
    str1=str1+str("梯形：%.10e"%(complex_T(y,a=0,b=10)))+" "+"&"+" "
    str1=str1+str("抛物线：%.10e"%(complex_S(y,a=0,b=10)))+" "+"&"+" "
    str1=str1+str("柯特斯：%.10e"%(complex_C(y,a=0,b=10)))
    str1=str1+str('\n')
print(str1)