#include <stdio.h>

/*this function gives equation of line of regression */
void equation(float X[],float Y[],int n,FILE *fp){
    float Sx=0,Sy=0;
    float Sx2=0,Sxy=0;
    float a_1,a_0;
    for(int i=0;i<n;i++){
        Sx=Sx+X[i];
    }
    for(int i=0;i<n;i++){
        Sy=Sy+Y[i];
    }
    for(int i=0;i<n;i++){
        Sx2=Sx2+(X[i]*X[i]);
    }
   for(int i=0;i<n;i++){
        Sxy=Sxy+(X[i]*Y[i]);
    }
     a_1=(n*Sxy-(Sx*Sy))/(n*Sx2-(Sx*Sx));

     a_0=(Sy-a_1*Sx)/(n);
     fprintf(fp,"%f",a_1);
     fprintf(fp,"\n");
     fprintf(fp,"%f",a_0);
     
     return;
}

/*In c language linked lists are present so i took x any y seperately linking them with index i*/
int main(){
    FILE*fp;
    fp=fopen("coefficents.dat","w");
    float X[]={1,2,3,4,5};
    float Y[]={7,6,5,4,3};
     int n=5;
    equation(X,Y,n,fp);

    return 0;
}