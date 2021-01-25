#let the two sides of the traingle are l and have a fixed base b p is perpendicular
from sympy import *
l=symbols('l')
b=symbols('b')
p=symbols('p')
A=symbols('A')
t=symbols('t')
init_printing(use_unicode=True)
#using PGT
p=pow(l**2-(b/2)**2,1/2)
A=1/2*(p*b)
k=diff(A,l)*3
m=k.subs(l,b)
s=simplify(m)
print("dA/dt={}".format(s))
