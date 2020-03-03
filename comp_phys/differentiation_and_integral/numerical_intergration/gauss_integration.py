import math
def y(x):
    if x==0:
        y=1
    else:
        y=math.sin(x)/x
    return y
#1阶高斯积分
def Gauss_1(y,a,b):
    x=math.sqrt(3)/3
    G=(y((a+b)/2+x*(a-b)/2)+y((a+b)/2-x*(a-b)/2))*(b-a)/2
    return G
#2阶高斯积分
def Gauss_2(y,a,b):
    x=math.sqrt(15)/5
    G=(8/9*y((a+b)/2)+5/9*(y((a+b)/2+x*(a-b)/2)+y((a+b)/2-x*(a-b)/2)))*(b-a)/2
    return G

def Complex_G1(y,a,b):
    G=0
    for i in range(n):
        x=a+i*h
        G=G+Gauss_1(y,x,x+h)
    return G
def Complex_G2(y,a,b):
    G=0
    for i in range(n):
        x=a+i*h
        G=G+Gauss_2(y,x,x+h)
    return G
a=0;b=10
str1=""
for i in [3,4,6,8,10]:
    n=2**i
    h=(b-a)/n
    str1=str1+str("一阶高斯=%.10e"%(Complex_G1(y,a,b)))+" "+"&"+" "
    str1=str1+str("二阶高斯=%.10e"%(Complex_G2(y,a,b)))
    str1=str1+'\n'
print(str1)
    
