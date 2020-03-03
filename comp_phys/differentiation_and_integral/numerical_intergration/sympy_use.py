from sympy import *
import mpmath
x = symbols("x")  # 符号x，自变量
for l in [5,10,50,100]:
    f1=cos(l*x)/sqrt(1+x**2)
    print(complex(integrate(f1,(x,-oo,+oo))))
    f2=exp(mpmath.j*l*(x+x**2))/sqrt(x)
    print(complex(integrate(f2,(x,0,1))))
