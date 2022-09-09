#include <stdio.h>
// return value is void 
void main()
{
    int nline = 0;
    int c; // stores that char that getchar returns
    // getchar reads from the center and imputs one character at a time
    // keep reading characters
    while ((c=getchar()) != EOF)
    {
        // test if the varaible c
        if (c == '\n')
        {
            nline++;
        }
    }
    // insert an int value 
    printf("Number of lines: %d\n", nline);
}