import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math


#Plotting the hyperbola
len=100
O=np.array([0,0])

theta = np.loadtxt('theta.dat',dtype='double')
k=np.loadtxt('eigen.dat',dtype='double')
y = np.zeros((2,len))
a=1/(k[0]**0.5)
b=1/((-k[1])**0.5)
y[0,:] = a*(1/np.cos(theta))
y[1,:] = b*np.tan(theta)

#Plotting the  normal
P=np.loadtxt('data/p.dat',dtype='double')
B=np.loadtxt('B.dat',dtype='double')
len =50

x_P = np.zeros((2,len))
lam_1 = np.linspace(-1,1,len)

for i in range(len):

    temp1 = P + lam_1[i]*(B-P)

    x_P[:,i]= temp1.T
    
plt.plot(x_P[0,:],x_P[1,:],label='Normal') 
plt.plot(P[0], P[1], 'o')
    
plt.plot(y[0,:],y[1,:],label='Hyperbola')
plt.plot(O[0], O[1], 'o')

plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')

plt.legend(loc="best")
plt.axis('equal')
plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.show()
plt.plot(x[0,:len],x[1,:len],color='r',label='Hyperbola')
plt.plot(x[0,len+1:],x[1,len+1:],color='r')

#Plotting the Normal
P = np.array([8,3*(3**0.5)]) 
B = np.array([25/2,0]) 
len =10

x_PB= np.zeros((2,len))
lam = np.linspace(-0.5,1,len)
for i in range(len):
  temp1 = P + lam[i]*(B-P)
  x_PB[:,i]= temp1.T
  
#Plotting the Tangent
C = np.array([2,0]) 
len =10

x_PC = np.zeros((2,len))
lam = np.linspace(-0.5,1,len)
for i in range(len):
  temp1 = P + lam[i]*(C-P)
  x_PC[:,i]= temp1.T 
#PLotting the point on the hyperbola 
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P') 
 
#PLotting the Lines on the hyperbola
plt.plot(x_PB[0,:],x_PB[1,:],label='$Normal$')
plt.plot(x_PC[0,:],x_PC[1,:],label='$Tangent$')
plt.grid() 
ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')

plt.show()
