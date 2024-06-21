#include<stdio.h>

int main()
{
    char alpha;
    printf("Enter char....");
    scanf("%c", &alpha);
    
    if(alpha>='A' && alpha<='Z')
    {
        printf("This is capital");
    }
    else if (alpha>='a' && alpha<='b')
    {
        printf("This is small");
    }
    
    return 0;
}