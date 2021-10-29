//
// Created by Alexandre Haddad-Delaveau on 9/23/21.
//

#include <cs50.h>
#include <stdio.h>
#include <math.h>

void printRow(int size, int spaces)
{
    // Calculate spaces required
    spaces = spaces - size;

    // Print spaces
    for (int i = 0; i < spaces; i++)
    {
        printf(" ");
    }

    // Print first star
    int printed = 1;
    printf("*");

    // Print additional stars
    while (printed < size)
    {
        printed++;
        printf(" *");
    }

    // Print new line
    printf("\n");

}

int main()
{
    // Get input between 1 and 20
    int rows;
    do
    {
        rows = get_int("Size: ");
    }
    while (rows < 1 || rows > 20);

    // Calculate spacing
    int spacing;
    if (rows % 2 == 1)
    {
        spacing = trunc(rows / 2) + 1;
    }
    else
    {
        spacing = rows / 2;
    }

    // Calculate length
    int length = trunc(rows / 2);

    // Setup temporary measurement variable
    int current_length = 1;

    // Print increasing in size portion
    while (current_length <= length)
    {
        printRow(current_length, spacing);

        current_length++;
    }

    // Create middle column (if odd)
    if (rows % 2 == 1)
    {
        printRow(spacing, spacing);
    }

    // Adjust for extra ++
    current_length--;

    // Print decreasing portion
    while (current_length > 0)
    {
        printRow(current_length, spacing);

        current_length--;
    }
}
