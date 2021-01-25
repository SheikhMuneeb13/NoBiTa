#given volume of tank=8m**3 depth=2m cost of building the base of tank is Rs 70/sq mtrs and Rs 4/sqr mtr for building sides
#let x,y,z be length ,breadth,depth of tank resp.
from sympy import *
x=symbols('x')
y=symbols('y')
z=symbols('z')
#let v denote volume of tank
v=symbols('v')
vc=symbols('vc')
init_printing(use_unicode=True)
v=x*y*z
l=v.subs(z,2)
voleq=Eq(l,8)
q=solve(voleq,y)
#let vc denote curved surface area of tank and Ac denote area of base
Ac=x*y
vc=symbols('vc')
vc=2*(2*x+2*y)
vc.simplify()
vc=vc.subs(y,q[0])
#total cost of curved sides=Tc
Tc=symbols('Tc')
Tc=vc*45
a=diff(Tc,x)
w=solve(a,x)
l=l.subs(x,w[1])
l=Eq(l,8)
e=solve(l,y)
#Now total cost is
Tc=Tc.subs(x,w[1])
Tc=Tc.subs(y,e[0])
Ac=Ac.subs(x,w[1])
Ac=Ac.subs(y,e[0])
#let Tb denote cost for base
Tb=Ac*70
#let TT denote total cost
TT=Tb+Tc
print(f"the value of x and y is    {w[1]} and  {e[0]} respectively and the total cost required is  {TT}")
