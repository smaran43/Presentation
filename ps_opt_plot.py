#Plotting The Curves For f(x)=x**3-3xc
import numpy as np
import matplotlib.pyplot as plt

#Plotting The Curves For Different Values Of c

#c=2
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=2', linestyle='-')

a=1
b=0
c=-6
d=0
curve_cubic(a,b,c,d)

#c=4
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=4', linestyle='-')
a=1
b=0
c=-12
d=0
curve_cubic(a,b,c,d)

#c=6
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=6', linestyle='-')
a=1
b=0
c=-18
d=0
curve_cubic(a,b,c,d)

#c=0
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=0', linestyle='-')
a=1
b=0
c=0
d=0
curve_cubic(a,b,c,d)

#c=-2
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=-2', linestyle='-')
a=1
b=0
c=6
d=0
curve_cubic(a,b,c,d)

#c=-4
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=-4', linestyle='-')
a=1
b=0
c=12
d=0
curve_cubic(a,b,c,d)

#c=-6
def curve_cubic(a,b,c,d,):
	x=list(range(-10,11))
	y=[(a*(i**3)+b*(i**2)+c*i+d) for i in x]
	plt.plot(x,y,label='Cubic Equation For c=-6', linestyle='-')
a=1
b=0
c=18
d=0
curve_cubic(a,b,c,d)

plt.legend(loc='best')
plt.grid()
plt.show()
