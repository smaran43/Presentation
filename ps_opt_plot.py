import numpy as np
import matplotlib.pyplot as plt

def curve_cubic(a,b,c,d):
	x=list(range(-10,11))
	y=[(a*i**3+b*i**2+c*i+d) for i in x]
	plt.plot(x,y,label='cubic', linestyle='-')

a=1
b=0
c=-6
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=-12
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=-18
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=0
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=6
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=12
d=0
curve_cubic(a,b,c,d)

a=1
b=0
c=18
d=0
curve_cubic(a,b,c,d)

plt.grid()
plt.show()
