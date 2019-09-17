#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


 int  main(void)
{
	
//Defining variables	
    
    double len,k,m;
    m = -2/sqrt(5);
    len = 1000;
    
    
//Defining Files
    FILE *fx;
    FILE *fy;
    FILE *fz;
    
    
//Opening Files w.r.t its names
    
    fx = fopen("xvalues.dat","w");
    fy = fopen("yvalues.dat","w");
    fz = fopen("zvalues.dat","w");
    
//Creating loop for finding x and y values
    for(int i = 0;i<len;i++)
    {
		k = -20 + (i*40)/(len-1);
		
		//For creating x values
		fprintf(fx,"%lf\n",k);
		//For creating y values
		fprintf(fy,"%lf\n",(3*pow(k,2)+72)/4);
        //For creating z values
        fprintf(fz,"%lf\n",m*k+7*sqrt(3));
	}
	
//Closing and saving .dat files
    fclose(fx);
    fclose(fy);
    fclose(fz);
 
    
	return 0;
	
}
