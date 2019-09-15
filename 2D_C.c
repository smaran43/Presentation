#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs1.h"

int  main() //main function begins
{

//Defining the variables
int m,n;
double **u,**p,**mat,**V,**q, r, **O, **N,**X;


//Given points
p = loadtxt("data/p.dat",2,1);

//Matrix equation
mat = loadtxt("data/mat.dat",2,2);
V = loadtxt("data/V.dat",2,2);
u=createMat(2,1);
*u[0]=0;
*u[1]=0;

//finding q(n) using the equation n=Vp+u
O = matmul(V,p,2,2,1);
q=linalg_add(O,u,2,1);

//finding normal vector to the equation of normal of hyperbola
N = matmul(mat,O,2,2,1);
X = matmul(transpose(N,2,1),p,1,2,1);

//The equation of normal  
printf("Equation of normal to hyperbola at point p is \n");
print(transpose(N,2,1),1,2);
printf("x=");
print(X,1,1);
  
//Normal vector of normal
printf("normal vector N = \n");
print(N,2,1);
}
