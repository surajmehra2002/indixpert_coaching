#include<stdio.h>

int main(){

    int number[10] = {12,43,45,2,3,9,12,80,10,20};
    printf("Dubble digit number list are: ");
    for (int i = 0; i < 10; i++)
    {
        if(number[i]>=10){
            printf("%d \t", number[i]);

        }
    }
    
    
    return 0;
}