import math
def y(x):
    if x==0:
        y=0
    else:
        y=(math.e**x-1)/(math.sqrt(x))
    return y
def y1(x):
    if x==0:
        y=0
    else:
        y=math.sin(x)/math.sqrt(x)
    return y
def Complex_G2(y,a,b):
    G=0
    for i in range(n):
        x=a+i*h
        G=G+Gauss_2(y,x,x+h)
    return G
def Gauss_2(y,a,b):
    x=math.sqrt(15)/5
    G=(8/9*y((a+b)/2)+5/9*(y((a+b)/2+x*(a-b)/2)+y((a+b)/2-x*(a-b)/2)))*(b-a)/2
    return G
def C_integrate(y,a,b):
    h=(b-a)/4
    C=(b-a)*(7/90*(y(a)+y(b))+16/45*(y(a+h)+y(a+3*h))+2/15*y(a+2*h))
    return C
def complex_C(y,a,b):
    C=0
    for i in range(int(n/4)):
        x=a+4*i*h
        C=C+C_integrate(y,x,x+4*h)
    return C 
a=0;b=1
str1=""
for i in [3,4,6,8,10,12]:
    n=2**i
    h=(b-a)/n
    result_gauss=Complex_G2(y,a,b)+2
    result_cotes=complex_C(y,a,b)+2
    str1=str1+str("h={:.3e},高斯积分结果={:.10f},柯特斯积分结果={:.10f}".format(h,result_gauss,result_cotes))
    str1=str1+'\n'
print(str1)
str2=""
for i in [3,4,6,8,10,12]:
    n=2**i
    h=(b-a)/n
    result_gauss=Complex_G2(y1,a,b)+2
    result_cotes=complex_C(y1,a,b)+2
    str2+=str("h={:.3e},高斯积分结果={:.10f},柯特斯积分结果={:.10f}".format(h,result_gauss,result_cotes))
    str2+='\n'
print(str2)