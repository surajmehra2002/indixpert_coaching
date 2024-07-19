#include<stdio.h>

int sum(int a, int b);   /* declaration of method , it always should be before main method*/  


void main(){

    int a = sum(12,4);    /* sum(12,4) is calling of method*/
    printf("%d",a);  
}

int sum(int a, int b){    /* line no 10 to 13 called definition of method*/
    return a+b;

}