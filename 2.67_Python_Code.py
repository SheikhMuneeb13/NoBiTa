#let the two sides of the traingle are l and have a fixed base b p is perpendicular
from sympy import *
from fractions import Fraction
l=symbols('l')
b=symbols('b')
p=symbols('p')
A=symbols('A')
t=symbols('t')
kl=symbols('kl')
init_printing(use_unicode=True)
#using PGT
p=pow(l**2-(b/2)**2,1/2)
#print(p)
A=1/2*(p*b)
k=diff(A,l)*3
m=k.subs(l,b)-kl
s=solve(m,kl)
s=s[0]
#rationalising the result
s=s*sqrt(b**2)
s=simplify(s)
s=s/b
#simplifing the result
sa=simplify(s)
print("dA/dt={}".format(sa))
