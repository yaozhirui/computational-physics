import math
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
print(o_path)
import Python_files.chap4.Piecewise.Spline_pro as Spline_pro
def y(x):
    y=x**3*math.log(x*a)/3-x**3/9
    return y
def exact_dy(x):
    exact_dy=x**2*math.log(a*x)
    return exact_dy
#九点三次样条插值求导,求x处的导数
def Spline_type_dy(x_,y_,x):
    d2y_=Spline_pro.Caculate_d2y_(x_,y_)
    for i in range(len(x_)):
        if x>=x_[i]:
            n=i
    if n==len(x_)-1:
        n=n-1
    S=-(x_[n+1]-x)**2*d2y_[n]/(2*h)+(x-x_[n])**2*d2y_[n+1]/(2*h)+(y_[n+1]-y_[n])/h-(d2y_[n+1]-d2y_[n])*h/6
    return S
def List_generate():
    x_=[]
    y_=[]
    for i in range(2*k+1):
        x_.append(x+(i-k)*h)
        y_.append(y(x_[i]))
    return x_,y_

x=1;a=2;k=4
str1=""
for i in [-1,-2,-3,-4,-6]:
    h=10**i
    x_,y_=List_generate()
    Spline_dy=Spline_type_dy(x_,y_,x)
    str1=str1+str("h=%.3e"%h)+" "+"&"+" "
    str1=str1+str("%.3e"%(Spline_dy-exact_dy(x)))+" "+"&"+" "
    str1=str1+'\n'
print(str1)