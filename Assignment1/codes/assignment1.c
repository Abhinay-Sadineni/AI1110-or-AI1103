#include <stdio.h>
#include <stdlib.h>

/*This code excatly follows the theory */
/*function to write data of point in the dat file*/
void put_data(float P[],int k,FILE*fp ){
    for(int i=0;i<k;i++){
              fprintf(fp,"%f ",P[i]);
          }
          fprintf(fp,"\n");
          return;
}

/*Dot product of two vectors*/
float dot(float a[],float b[],int k){
              float pro=0;
              for(int i=0;i<k;i++){
                  pro=pro+a[i]*b[i];
              }
              return pro;
}

/*Normal function for square of norm of a vector*/
float sqnorm(float n[],int k){
    float w=0;
    for(int i=0;i<k;i++){
           w=w+n[i]*n[i];
    }
    return w;
}

/*Using the image formula we can get relected points and put them in dat file*/
void reflect( int k,float n[],float c,float P[],FILE*fp){

          float*R;
          R =(float*)malloc(sizeof(float)*k);

          for(int i=0;i<k;i++){
              R[i]=P[i]+2*((c-dot(n,P,k))/(sqnorm(n,k)))*n[i];
          }
          put_data( R, k,fp );
          free(R);
          return  ;
}


int main(){
    FILE*fp;
    fp=fopen("points.dat","w");
    float A[]={0,4};
    float B[]={2,3};
    float C[]={1,1};
    float D[]={2,0};

/*normal vector of y-axis and constant c*/
    float n[]={1,0};
    float c=0;

/*k represent the no of dimesions like 2D or 3D*/
    int k=2;

/*Putting the points in dat file*/
  put_data( A, k,fp );
  put_data( B, k,fp );
  put_data( C, k,fp );
  put_data( D, k,fp );

/*Now putting the reflected points in the dat file*/
    reflect(k,n,c,B,fp);
    reflect(k,n,c,C,fp);
    reflect(k,n,c,D,fp);

    fclose(fp);
    return 0;

}
