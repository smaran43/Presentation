#Program to plot teh required hyperbola
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 1000
theta = np.linspace(-5,5,len)

#Given hyperbola parameters
#Eqn : x.T@V@x = F
V = np.array(([9,0],[0,-16]))
F = 144

#Standard Eqn : y.T@D@y=1
#comparing these equations, get :  
#y = P.T@x/sqrt(F)
#P.T@V@P = D
#P.T@P = I

eigval,eigvec = LA.eig(V)
print(eigval)
print(eigvec)

D = np.diag(eigval)
P = eigvec
print("D=\n",D)
print("P=\n",P)


#Generating points on the hyperbola at origin
y = np.zeros((2,len))
y[0,:] = 1/eigval[0]*np.cosh(theta)
y[1,:] = 1/eigval[1]*np.sinh(theta)

#Standard hyperbola : y.T@D@y=1
y1 = np.linspace(-1,1,len)
y2 = np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y3 = -1*np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y = np.hstack((np.vstack((y1,y2)),np.vstack((y1,y3))))

#Affine Transformation
#Equation : y = P.T@(x-c)/(K**0.5)
x = (P @ (y)) * F**0.5

#Plotting required hyperbola
plt.plot(x[0,:len],x[1,:len],color='r',label='Hyperbola')
plt.plot(x[0,len+1:],x[1,len+1:],color='r')

P = np.array([8,3*(3**0.5)]) 
B = np.array([25/2,0]) 
len =10

x_PB= np.zeros((2,len))
lam = np.linspace(-0.5,1,len)
for i in range(len):
  temp1 = P + lam[i]*(B-P)
  x_PB[:,i]= temp1.T
  
C = np.array([2,0]) 
len =10

x_PC = np.zeros((2,len))
lam = np.linspace(-0.5,1,len)
for i in range(len):
  temp1 = P + lam[i]*(C-P)
  x_PC[:,i]= temp1.T 
  
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P') 
  
plt.plot(x_PB[0,:],x_PB[1,:],label='$Normal$')
plt.plot(x_PC[0,:],x_PC[1,:],label='$Tangent$')
plt.grid() 
ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')

# #if using termux
#plt.savefig('../figs/hyperbola.pdf')
#plt.savefig('../figs/hyperbola.eps')
#subprocess.run(shlex.split("termux-open ../figs/hyperbola.pdf"))
#else

plt.show()
