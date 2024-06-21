
// write a program to input user marks and print there percantage with first , second , third 
#include<stdio.h>
int main()
{
    char name[10];
    int hin_mark, eng_mark, math_mark, sci_mark,com_mark;
    float totle_per;

   
    printf("\n\nplease enter your name ");
    scanf("%s", &name);
    
    printf("Enter your hindi marks ");
    scanf("%d", &hin_mark);

    printf("Enter your english marks ");
    scanf("%d", &eng_mark);

    printf("Enter your math marks ");
    scanf("%d", &math_mark);

    printf("Enter your science marks ");
    scanf("%d", &sci_mark);

    printf("Enter your computer marks ");
    scanf("%d", &com_mark);

    if(hin_mark>100 || eng_mark>100 || math_mark>100 || sci_mark>100 || com_mark>100)
    {
        printf(" \n Sorry %s! please Enter all sub. mark between 0 to 100", name);
    }

    else
    {
        totle_per= (hin_mark+eng_mark+math_mark+sci_mark+com_mark)/5.0;

        if (totle_per>=80)
        {
            printf("Oh congratulation %s! You are first with %f %%",name, totle_per);
        }
        else if(totle_per>=60)
        {
            printf("Nice %s! You are second with %f %%",name, totle_per);
        }
        else if (totle_per>=30)
        {
            printf("%s, You are third  with %f %%",name, totle_per);
        }
        else 
        {
            printf("Sorry %s you have failed!  with %f %%",name, totle_per);
        }

    }


    
    return 0;
}