#include <stdio.h>
#define RED "\x1B[31m"
#define GREEN "\x1B[32m"
#define YEL "\e[0;33m"
#define RESET "\x1B[0m"
int main()
{
    int task, exit = 1;
    int deposit, withdraw;

    char name[20];
    long long int account_no = 0;
    int balance;

    printf("\n\n*********** Banking Management System ************\n");
    printf("\n1- Create Account");
    printf("\n2- Deposit");
    printf("\n3- Withdraw");
    printf("\n4- Check Balance");
    printf("\n0- Exit\n");

    while (exit != 0)
    {

        printf("\nPlease Enter the task number: ");
        scanf("%d", &task);

        

        if (task == 1)
        {
            if (account_no == 0)
            {

            create_account:
                printf("\nPlease Enter 11 digit Account Number only: ");
                scanf("%lld", &account_no);

                if (account_no > 10000000000 && account_no < 100000000000)
                {
                    printf("Please Enter your Account Holder Name: ");
                    scanf("%s", &name);

                input_balance:
                    printf("Please Enter Balance (Opening Account would be 500 minimum): ");
                    scanf("%d", &balance);

                    if (balance >= 500)
                    {
                        printf(GREEN "\nThank you to join india bank" RESET);
                        printf("\nyour account details:\n");
                        printf("Account Number: %lld\n", account_no);
                        printf("Account Holder Name: %s\n", name);
                        printf("Account Balance: %d\n\n", balance);
                    }
                    else
                    {
                        goto input_balance;
                    }
                }

                else
                {
                    printf("Please enter valid account no");
                    goto create_account;
                }
            }
            else
            {
                int press;
                printf("You have already account\n");
                printf("press--1 for new account \npress--2 for account information \npress--0 for exit\n");
                printf("press--");
                scanf("%d", &press);
                if (press == 1)
                {
                    goto create_account;
                }

                else if (press == 2)
                {
                    printf("Account Number: %lld\n", account_no);
                    printf("Account Holder Name: %s\n", name);
                    printf("Account Balance: %d\n\n", balance);
                }
                else if (press == 0)
                {
                    printf("Your access is previous account\n");
                }
            }
        }

        else if (task == 2)
        {

            if (account_no > 10000000000 && account_no < 100000000000)
            {
            depositmoney:
                printf("\nPlease Enter Deposite Balance -100: ");
                scanf("%d", &deposit);

                if (deposit >= 100)
                {
                    balance += deposit;
                    printf(GREEN "\n***Thanks for Using Us***" RESET);
                    printf(YEL "\nAccount Number = %lld" RESET, account_no);
                    printf(YEL "\n%d Rupeees has credited in Your account.\n" RESET, deposit);
                }
                else if (deposit < 100 && deposit != 0)
                {
                    printf(RED "Please Deposite Balance more than 100 (press--0 for exit):" RESET);
                    goto depositmoney;
                }
                else
                {
                    printf("You left");
                }
            }
            else
            {
                printf(RED "\nError - Sorry! Please Create Customer Account First....\n" RESET, deposit);
            }
        }

        else if (task == 3)
        {
            if (account_no > 10000000000 && account_no < 100000000000)
            {
                printf("Enter withdraw ammount: ");
                scanf("%d", &withdraw);
                if (balance > withdraw)
                {
                    balance -= withdraw;
                    printf(GREEN "\nAccount Number = %lld" RESET, account_no);
                    printf(GREEN "\n%d Rupees Debited in your Bank Account\n" RESET, withdraw);
                }
                else
                {
                    printf("Insufficient Balance in your Account\n");
                }
            }
            else
            {
                printf(RED "\nError - Sorry! Please Create Customer Account First....\n" RESET, withdraw);
            }
        }

        else if (task == 4)
        {
            if (account_no > 10000000000 && account_no < 100000000000)
            {
                printf(GREEN "\nAccount Number = %lld" RESET, account_no);
                printf(GREEN "\nYour account Balance is: %d\n" RESET, balance);
            }
            else
            {
                printf(RED "\nError - Sorry! Please Create Customer Account First....\n" RESET, balance);
            }
        }
        else if (task == 0)
        {
            exit = task;
        }

        else
        {
            printf("\nOhh! Please Enter valid task no\n");
            
        }
    }

    printf(RED "\nYou Have Left This Project" RESET);

    return 0;
}