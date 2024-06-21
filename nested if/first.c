#include<stdio.h>
int main()
{
    int num;
    printf("Enter no to check even or odd...");
    scanf("%d", &num);

    if(num>0)
    {
        if (num%2==0)
        {
            printf("Enterd no is even");
        }
        else{
            printf("Enterd no is odd");
        }
    }
    else
    {
        printf("please enter positive no");
    }


    return 0;
}