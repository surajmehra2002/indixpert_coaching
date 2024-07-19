#include<stdio.h>
int main()
{
    int num;
    

    while (1)
    {
        
        printf("\n\nEnter no. for checking: ");
        scanf("%d", &num);
        
        if(num>0)
        {
            printf("Entered no is positive");
            
        }
        else if(num==0)
        {
            printf("Entered no is Zero");

        }
        else{
            printf("Entered no is negative");
        }
    }
    return 0;
}