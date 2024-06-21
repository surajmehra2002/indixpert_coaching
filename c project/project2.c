#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter the number of students: ");
    scanf("%d", &n);
    
    int marks[n]; // Array to store marks
    printf("Enter the marks for each student:\n");
    
    for(i = 0; i < n; i++) {
        printf("Student %d: ", i+1);
        scanf("%d", &marks[i]);
    }
    
    // Initialize first and second to the minimum integer value
    int first = -1, second = -1;
    
    // Find first and second highest marks
    for(i = 0; i < n; i++) {
        if(marks[i] > first) {
            second = first;
            first = marks[i];
        } else if(marks[i] > second && marks[i] != first) {
            second = marks[i];
        }
    }
    
    printf("Highest mark is: %d\n", first);
    printf("Second highest mark is: %d\n", second);
    
    return 0;
}