#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);
int main(void)
{
    //prompt user for height (int)
    int height;
    do
    {
        height = get_int("Height: ");

    }
    while(height < 1 || height > 8);

    //print pyramid of that height
    for (int i = 1; i <= height; i++)
    {
        // 1. Print the necessary spaces for right-alignment
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }

        //print the bricks
        print_row(i);
    }
}

//Given a number of bricks, print that number of bricks
void print_row(int bricks)
{
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }

    printf("\n");
}
