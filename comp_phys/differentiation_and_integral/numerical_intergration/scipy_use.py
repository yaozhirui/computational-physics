from scipy import integrate
from mpmath import *
def f(x):
    y=cos(l*(x+x*2))/sqrt(x)
    return y
def f2(x):
    y=sin(l*(x+x*2))/sqrt(x)
    return y
str1=""
for l in [5,10,50,100]:
    u, err1= integrate.quad(f,0,1)
    v, err2= integrate.quad(f,0,1)
    str1=str1+str("结果=%s"%(u+j*v))
    str1=str1+'\n'
print(str1)
