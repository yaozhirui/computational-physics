import random
import math
def integral_MC1(z,x_min,x_max,y_min,y_max):
    S=0
    for i in range(n):
        x=random.uniform(x_min,x_max)
        y=random.uniform(y_min,y_max)
        S=S+z(x,y)
    S=S*(x_max-x_min)*(y_max-y_min)/n
    return S
def integral_MC2(z,x_min,x_max,y_min,y_max):
    count=0
    for i in range(n):
        x=random.uniform(x_min,x_max)
        y=random.uniform(y_min,y_max)
        z_min=0;z_max=4
        f=random.uniform(z_min,z_max)
        if f<z(x,y):
            count=count+1           
    S=count*(y_max-y_min)*(x_max-x_min)*(z_max-z_min)/n
    return S
def z(x,y):
    z=y*(4-y**2)**0.5
    return z
x_min=0;x_max=math.pi/2
y_min=0;y_max=2
str1=""
for i in [2,3,4,6]:
    n=10**i
    S1_error=integral_MC1(z, x_min, x_max, y_min, y_max)-4*math.pi/3
    S2_error=integral_MC2(z, x_min, x_max, y_min, y_max)-4*math.pi/3
    str1=str1+str("n={:.1e},误差1={:.10f},误差2={:.10f}".format(n,S1_error,S2_error))
    str1+="\n"
print(str1)