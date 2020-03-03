import math
def y(x):
    y=x**3*math.log(x*a)/3-x**3/9
    return y
def exact_dy(x):
    exact_dy=x**2*math.log(a*x)
    return exact_dy
def three_points_dy(y):
    three_points_dy=(y(x+h)-y(x-h))/(2*h)
    return three_points_dy
def five_points_dy(y):
    five_points_dy=(2/3*(y(x+h)-y(x-h))-1/12*(y(x+2*h)-y(x-2*h)))/h
    return five_points_dy
def seven_points_dy(y):
    seven_points_dy=(3/4*(y(x+h)-y(x-h))-3/20*(y(x+2*h)-y(x-2*h))
    +1/60*(y(x+3*h)-y(x-3*h)))/h
    return seven_points_dy
def nine_points_dy(y):
    nine_points_dy=(4/5*(y(x+h)-y(x-h))-1/5*(y(x+2*h)-y(x-2*h))
    +4/105*(y(x+3*h)-y(x-3*h))-1/280*(y(x+4*h)-y(x-4*h)))/h
    return nine_points_dy
x=1;a=2
str1=""
for i in [-1,-2,-3,-4,-6]:
    h=10**i
    str1=str1+str("h=%.3e"%h)+" "+"&"+" "
    str1=str1+str("%.3e"%(three_points_dy(y)-exact_dy(x)))+" "+"&"+" "
    str1=str1+str("%.3e"%(five_points_dy(y)-exact_dy(x)))+" "+"&"+" "
    str1=str1+str("%.3e"%(seven_points_dy(y)-exact_dy(x)))+" "+"&"+" "
    str1=str1+str("%.3e"%(nine_points_dy(y)-exact_dy(x)))
    str1=str1+str('\n')
print(str1)
