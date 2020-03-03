import math
def y(x):
    y=x**3*math.log(x*a)/3-x**3/9
    return y
def front_dy(y):
    front_dy=(y(x+h)-y(x))/h
    return front_dy
def back_dy(y):
    back_dy=(y(x)-y(x-h))/h
    return back_dy
def central_dy(y):
    central_dy=(y(x+h)-y(x-h))/(2*h)
    return central_dy
def exact_dy(x):
    exact_dy=x**2*math.log(a*x)
    return exact_dy
x=1;a=2
str1=""
for i in [-1,-2,-3,-4,-6]:
    h=10**i
    str1=str1+str("h=%.3e"%h)+" "+"&"+" "
    str1=str1+str("front_error=%.3e"%(front_dy(y)-exact_dy(x)))+" "+"&"+" "
    str1=str1+str("back_error=%.3e"%(back_dy(y)-exact_dy(x)))+" "+"&"+" "
    str1=str1+str("center_error=%.3e"%(central_dy(y)-exact_dy(x)))
    str1=str1+str('\n')
print(str1)
    

