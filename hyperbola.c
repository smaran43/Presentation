#include<stdio.h>
//Declaring the order of matrices
float v[2][2];
float i,j;
float n[2][1];
float u[2][1];
float p[2][1];
float N[2][1];
float NT[1][2];
float y;
int main(){
	//Matrix V
    v[0][0]=9;
    v[0][1]=0;
    v[1][0]=0;
    v[1][1]=-16;
    
    //Matrix p
    p[0][0]=8;
    p[1][0]=5.19615;
    //Matrix u
    u[0][0]=0;
    u[1][0]=0;
    //Finding n from n=Vp+u
    n[0][0]=v[0][0]*p[0][0]+u[0][0];
    n[1][0]=v[1][1]*p[1][0]+u[1][0];
    //Matrix N - Normal vector
    N[0][0]=-n[1][0];
    N[1][0]=n[0][0];
    //(N^T)*P RHS of the normal equation
    y=(N[0][0]*p[0][0])+(N[1][0]*p[1][0]);
    //Matrix N^T
    NT[0][0]=N[0][0];
    NT[0][1]=N[1][0];
    
    printf("Equation of normal to hyperbola is \n");
    printf("(%f    ",NT[0][0]);
    printf("%f) ",NT[0][1]);
    printf("x=%f\n",y);
    printf("normal vector N=(%f)\n",N[0][0]);
    printf("                (%f)",N[1][0]);
}

