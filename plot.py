import numpy as np
import scipy
import mpmath as mp
import matplotlib.pyplot as plt

O = np.array([0,0])
x = np.loadtxt('xvalues.dat',dtype='double')
y = np.loadtxt('yvalues.dat',dtype='double')
z = np.loadtxt('zvalues.dat',dtype='double')
k = 0*np.ones(1000)


plt.plot(x,y,label="$Hyperbola")
plt.plot(x,z,label="$Normal1$")
plt.plot(k,y)
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O') 
plt.grid() 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.axis('equal')
plt.xlim((-60,60))
plt.ylim((-40,40))
plt.show() 
