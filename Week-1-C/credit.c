#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card = get_long("Number: ");
    int sum = 0, count = 0;
    long temp = card;
    long first_two = 0;

    while (temp > 0)
    {
        int digit = temp % 10;

        if (count % 2 == 0) // Every other starting from last
        {
            sum += digit;
        }
        else // Every other starting from second-to-last
        {
            int product = digit * 2;
            sum += (product / 10) + (product % 10);
        }

        if (temp >= 10 && temp < 100) first_two = temp; // Capture starting digits

        temp /= 10;
        count++;
    }

    // Checksum + Length + Starting Digits
    if (sum % 10 == 0)
    {
        if (count == 15 && (first_two == 34 || first_two == 37)) printf("AMEX\n");
        else if (count == 16 && (first_two >= 51 && first_two <= 55)) printf("MASTERCARD\n");
        else if ((count == 13 || count == 16) && (first_two / 10 == 4)) printf("VISA\n");
        else printf("INVALID\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
