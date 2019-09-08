#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
double * s ; 
//Uniform random numbers
s = uniform("uni.dat", 1000000);
double g=0;
//double g=0;

for (int i = 0; i < 1000000; i++){
	f+=s[i];
	
}
double a;
a=f/1000000;
double g=1;
for (int i = 0; i < 1000000; i++){
g+=(s[i] - a)*(s[i] - a);
}
g/=1000000;

printf("Mean = %lf\n",a);
printf("Variance = %lf\n",g);


return 0;
}
