#include<stdio.h>

int main(){

    int number;
    while(number!=0)
    {
    printf("\n\nEnter your mask: ");
    scanf("%d", &number);

        if (number>100)         
        {
            printf("Oh! Please enter valid mask");
        }

        else if (number>=60 && number<=100 )
        {
            printf("Congratulation! You are first");
        }

        else if (number>=40 && number<60 )
        {
            printf("You are second");
        }
        
        else if (number>=30 && number<40 )
        {
            printf("You are third");
        }
        
        else if (number<30)
        {
            printf("You are Fail! please word hard for batter");
        }
        
        
    }
    
    return 0;
}