#include <stdio.h>

/*this function gives equation of line of regression */
void equation(float X[],float Y[],int n){
    float Sx=0,Sy=0;
    float Sx2=0,Sxy=0;
    float byx,a;
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
     byx=(n*Sxy-(Sx*Sy))/(n*Sx2-(Sx*Sx));

     a=(Sy-byx*Sx)/(n);
     if(byx<0){printf("Y+%fX=%f",-byx,a);}
     else{printf("Y=%f+%fX",a,byx);}
     return;
}

/*In c language linked lists are present so i took x any y seperately linking them with index i*/
int main(){
    float X[]={1,2,3,4,5};
    float Y[]={7,6,5,4,3};
     int n=5;
    equation(X,Y,n);
    return 0;
}