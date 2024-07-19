
// C programm to take no form user in print that is even or odd

#include <stdio.h>
 
int main(){

 int num;
 printf("\nEnter no for check even or odd ");
 scanf("%d", &num);

 if(num%2!=0){
    printf("This is odd number\n");
 }
 else{
    printf("This is even number\n");
 }
 
 return 0;
}
