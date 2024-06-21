#include<stdio.h>
int main()
{
    int n, i;
    printf("Enter the number of student");
    scanf("%d", &n);

    int marks[n];


    printf("Enter the marks for each student \n");

    for (i=0;i<n;i++)
    {
        printf("student %d:", i+1);
        scanf("%d",&marks[i]);

    }
    for (i = 0; i < n; i++)
    {
        printf("%d \n",marks[i]);
    }
    


    return 0;
}