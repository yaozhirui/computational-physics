from mpmath import *
from scipy import integrate
def f1(x):
    if x==0:
        y=0
    else:
        y=(exp(j*l*(x+x*2))-1)/sqrt(x)
    return y
def f2(x):
    y=exp(-j*l*x)/sqrt(1+x**2)
    return y
def f1_Re(x):
    y=cos(l*(x+x*2))/sqrt(x)
    return y
def f1_Im(x):
    y=sin(l*(x+x*2))/sqrt(x)
    return y
#2阶高斯积分
def Gauss_2(y,a,b):
    x=sqrt(15)/5
    G=(8/9*y((a+b)/2)+5/9*(y((a+b)/2+x*(a-b)/2)+y((a+b)/2-x*(a-b)/2)))*(b-a)/2
    return G
def Complex_G2(y,a,b):
    G=0
    h=(b-a)/n
    for i in range(n):
        x=a+i*h
        G=G+Gauss_2(y,x,x+h)
    return G
def saddle_method_I1(y):
    G=exp(j*pi/4)*sqrt(pi/l)
    return G
def infinite_I(y):
    pre=1e-4;a=0;I=0;T=1
    while (fabs(T)>pre):
        T=Complex_G2(y,a,a+1)
        I=I+T
        a=a+1
    return I
def saddle_method_I2(y):
    I=0
    return I
str1=""
for l in [5,10,50,100]:
    n=2**12
    gauss_result=Complex_G2(f1,a=0,b=1)+2
    saddle_result=saddle_method_I1(f1)
    exalt_result=integrate.quad(f1_Re,a=0,b=1)[0]+j*integrate.quad(f1_Im,a=0,b=1)[0]
    str1=str1+str("准确结果=%s，高斯结果=%s，鞍点法结果=%s"%(exalt_result,gauss_result,saddle_result))
    str1=str1+'\n'
print(str1)
str2=""
for l in [5,10,50,100]:
    n=4*l
    gauss_result=infinite_I(f2)
    saddle_result=saddle_method_I2(f2)
    exalt_result=0
    str2=str2+str("准确结果=%s，高斯结果=%s，鞍点法结果=%s"%(exalt_result,gauss_result,saddle_result))
    str2=str2+'\n'
print(str2)


