/*All header files which used in this programm*/
#include <stdio.h>      /* use for printf(), scanf() ...*/
#include <string.h>     /* use for string methods strcmp(), strcpy()...*/
#include <stdlib.h>     /* use for atoi() for convert string to int*/

/*text color code for different output*/ 
#define RED "\x1B[31m"
#define GREEN "\x1B[32m"
#define YEL "\e[0;33m"
#define RESET "\x1B[0m"


/*All globle variable*/ 
char books[10][50];
char authors[10][50];
char borrow_list_books[10][50];
char borrow_list_authors[10][50];

int Available_book = 0;
int Borrowed_book = 0;
    

/*function declearation*/
void add_book();     
void display_book();     
void borrow_book();     
void return_book();     
void search_by_title();   
void search_by_authors();


// Function run for press 1 when add new book
void add_book()           
{
    
    char title[50];
    char author[50];
    
    valid_book:
        do
        {
            printf("Enter the title of the book: ");
            gets(title);   /*to take string form user with space*/        
        } while (strcmp(title,"")==0);
        
   if (atoi(title))   /*atoi() method convert string to int, if convertable then true otherwise false*/
        {
            printf(RED"\nError! integer book name not allowed\n"RESET);
            goto valid_book;
        }

    
     valid_name:
        do
        {      
            printf("Enter the author of the book: ");
            gets(author);  /*to take string form user with space*/
        
        } while (strcmp(author,"")==0);

    if (atoi(author) )
            {
                printf(RED"\nError! author name cant't be integer \n"RESET);
                goto valid_name;
            }
    

    // copy entered book in 2D char array
    strcpy(books[Available_book], title);
    strcpy(authors[Available_book], author);
    
    printf(GREEN"Book added successfully!\n"RESET);
    Available_book+=1;
    

}

// Function run for press 2 when display available books in library
void display_book()           
{
   
    if(Available_book==0){
        printf(YEL"Sorry! No books available in library, Press 1 for add new...\n"RESET);
    }
    else{
        printf("Available books are: ");
        printf("\n=======================================================================\n");
        printf("Title\t\t\t\t\t Author");
        printf("\n=======================================================================\n");

        for (int i = 0; i < Available_book; i++)
        {
            printf("%d.%s\t\t\t\t%s",i+1, books[i], authors[i]);
            printf("\n");
        }
        printf("=======================================================================\n");
    }


}

// Function run for press 3 when Borrow from library 
void borrow_book()      
{   
    int access = 0, access1=0;
    char borrow[20];
   
   

        valid_borrow:
        do
        {
            printf("Enter the title of the book you want to Borrow: ");
            gets(borrow);   /*to take string form user with space*/        
        } while (strcmp(borrow,"")==0);
        
   if (atoi(borrow))   /*atoi() method convert string to int, if convertable then true otherwise false*/
        {
            printf(RED"\nError! integer book name not allowed\n"RESET);
            goto valid_borrow;
        }

    

   for (int i=0; i<Available_book; i++)
   {    
        if(strcmp(books[i],borrow) == 0)
        {      
            for (int j=0; j<3;j++)
            {
                if (strcmp(borrow_list_books[j], "")==0)
                {
                    strcpy(borrow_list_books[j], books[i]);
                    strcpy(borrow_list_authors[j], authors[i]);
                    break;
                }
                if (strcmp(borrow_list_books[j], "")!=0 && j==5)
                {
                    printf(RED"\nSorry! Lot's of books are borrow! After return those books tri to borrow \n"RESET);
                }
                
                
            }
            printf(GREEN"You have borrowed '%s' book which author name is %s\n"RESET,books[i],authors[i]);
            Available_book-=1;
            Borrowed_book+=1;
             for (int k = i; k < Available_book; k++)
                {
                    strcpy(books[k], books[k + 1]);
                    strcpy(authors[k], authors[k + 1]);
                }        
            access=1;  
            goto checking;     
                
        }  
   }
    for (int i = 0; i < Borrowed_book; i++)
    {
       if (strcmp(borrow_list_books[i],borrow)==0)
       {
        printf(YEL"%s book already borrow\n"RESET, borrow);
        access1=1;
        break;  
       }
       
    }
     
    checking :
        if (access==0 && access1==0)
        {
            printf(RED"No '%s' book available for borrow... \n"RESET, borrow);
        }
   
}

void return_book()
{
    char return_borrow[20];
   
    
    valid_return:
        do
        {
            printf("Enter the title of the book you want to return: ");
            gets(return_borrow);   /*to take string form user with space*/        
        } while (strcmp(return_borrow,"")==0);
        
   if (atoi(return_borrow))   /*atoi() method convert string to int, if convertable then true otherwise false*/
        {
            printf(RED"\nError! integer book name not allowed\n"RESET);
            goto valid_return;
        }


    
    for (int j = 0; j <= Borrowed_book; j++)
    {
        if (strcmp(borrow_list_books[j],return_borrow)==0)
        {
            printf(GREEN"\nYou have successfully returned '%s' book\n"RESET,borrow_list_books[j]);

            strcpy(books[Available_book], borrow_list_books[j]);
            strcpy(authors[Available_book], borrow_list_authors[j]);
            
            Available_book++; 
            for (int k = j; k < Borrowed_book; k++)
                {
                    strcpy(borrow_list_books[k], borrow_list_books[k + 1]);
                    strcpy(borrow_list_authors[k], borrow_list_authors[k + 1]);
                }    
            
            Borrowed_book-=1;
            break;
        }
        else if (strcmp(borrow_list_books[j],return_borrow)!=0 && j==Borrowed_book)
        {
            printf(RED"No '%s' book found for return.\n"RESET, return_borrow);
        }
    }
    

    

}

// Function run for press 5 when search books using title 
void search_by_title()
{
    char search_title[50];
    int found = 0;

    do
    {
        printf("Enter the title of the book you want to search for: ");
        gets(search_title);
    } while (strcmp(search_title,"")==0);

    printf("\nSearch Book with title '%s':\n", search_title);
    printf("=======================================================================\n");
    printf("Title\t\t\t\t\t Author");
    printf("\n=======================================================================\n");

    for (int i = 0; i < Available_book; i++)
    {   
        // for(int j = 0; )
        if (strcmp(books[i], search_title) == 0)
        {
            printf(GREEN"%s\t\t\t\t"RESET, books[i]);
            printf("%s\n",authors[i]);
            found = 1;
        }
        
    }

    if (!found)
    {
        printf(RED"No books found with title '%s'.\n"RESET, search_title);
    }
    printf("=======================================================================\n");
}

// Function run for press 6 when search books using authors name 
void search_by_authors()
{
    char search_author[50];
    int found = 0;

    do
    {
        printf("Enter the author of the book you want to search for: ");    
        gets(search_author);
    } while (strcmp(search_author,"")==0);

    printf("\nSearch books with author '%s':\n", search_author);
    printf("=======================================================================\n");
    printf("Title\t\t\t\t\t Author");
    printf("\n=======================================================================\n");

    for (int i = 0; i < Available_book; i++)
    {
        if (strcmp(authors[i], search_author) == 0)
        {
            printf("%s\t\t\t\t", books[i]);
            printf(GREEN"%s\n"RESET,authors[i]);
            found = 1;
        }
        else{
            printf("Please enter valid book name \n");
        }
    }

    if (!found)
    {
        printf(RED"No books found with author '%s'.\n"RESET, search_author);
    }
    printf("=======================================================================\n");
}

int main ()
{
    int task;  

    printf("\n-----------------------------------------------------------------------------------------------------------------------------\n");

    printf(GREEN"\n\t************** Project 03 -  Library Management System **************\n\n"RESET);
    printf("\t\t1- Add New Book\n");
    printf("\t\t2- Display Available Books\n");
    printf("\t\t3- Borrow Book\n");
    printf("\t\t4- Return Book\n");
    printf("\t\t5- Search Book by title\n");
    printf("\t\t6- Search Book by Author\n");
    printf("\t\t0- Exit\n");
 
    do
    {
        task = 100;
        printf("\n-----------------------------------------------------------------------------------------------------------------------------");
        printf("\nPlease Enter The choice : ");
        scanf("%d", &task);
        getchar();

        if (task==1)
        {
            add_book();
        }

        else if (task==2)
        {
            display_book();        
        }
        else if (task==3)
        {
            borrow_book();
        }
        else if (task==4)
        {
            return_book(); 
        }
        else if (task==5)
        {
        search_by_title(); 
        }
        else if (task==6)
        {
        search_by_authors();
        }
        
        else if (task==0)
        {
            printf(GREEN"\nExiting Programm...........\n"RESET);
        }
        
        else
        {
            printf("Please enter valid task no (task 0 to 5)\n");
        }


    } while (task!=0);

    printf("You have left this project....");
    printf("\n__________________________________________________________________________________________________________________________________\n\n\n");
    return 0;
}