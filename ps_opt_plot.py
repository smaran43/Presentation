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

#Convexity/Concavity
def cub(x):
	return x**3

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

a = -5
b = 5
lamda = 0.3
c = lamda *a + (1-lamda)*b
f_a = cub(a)
f_b = cub(b)

f_c = cub(c)
f_c_hat = lamda *f_a + (1-lamda)*f_b

#Plot commands
plt.plot([a,a],[0,f_a],color=(1,0,0),marker='o',label="$f(a)$")
plt.plot([b,b],[0,f_b],color=(0,1,0),marker='o',label="$f(b)$")
plt.plot([c,c],[0,f_c],color=(0,0,1),marker='o',label="$f(\lambda a + (1-\lambda)b)$")
plt.plot([c,c],[0,f_c_hat],color=(1/2,2/3,3/4),marker='o',label="$\lambda f(a) + (1-\lambda)f(b)$")
plt.plot([a,b],[f_a,f_b],color=(0,1,1))

plt.legend(loc='best')
plt.grid()
plt.show()
