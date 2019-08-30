#Plotting the curve f(x)=x**3-3xc for different values of c
import numpy as np
import matplotlib.pyplot as plt

#Defining the cubic curve
def curve_cubic(a,b,c,d):
	x=list(range(-10,11))
	y=[(a*i**3+b*i**2+c*i+d) for i in x]
	plt.plot(x,y,label='cubic', linestyle='-')
#Putting different values of c

#c=2
a=1
b=0
c=-6
d=0
curve_cubic(a,b,c,d)

#c=4
a=1
b=0
c=-12
d=0
curve_cubic(a,b,c,d)

#c=6
a=1
b=0
c=-18
d=0
curve_cubic(a,b,c,d)

#c=0
a=1
b=0
c=0
d=0
curve_cubic(a,b,c,d)

#c=-2
a=1
b=0
c=6
d=0
curve_cubic(a,b,c,d)

#c=-4
a=1
b=0
c=12
d=0
curve_cubic(a,b,c,d)

#c=-6
a=1
b=0
c=18
d=0
curve_cubic(a,b,c,d)

plt.grid()
plt.show()
