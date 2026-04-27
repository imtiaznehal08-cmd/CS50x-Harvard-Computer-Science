#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function Prototypes
bool is_valid_numeric_key(string input);
char shift_character(char character, int shift_value);

int main(int argc, string argv[])
{
    // 1. Validate Command Line Arguments
    // We expect exactly one argument: the numeric key for the cipher
    if (argc != 2 || !is_valid_numeric_key(argv[1]))
    {
        printf("Error: Please provide a single numeric key.\n");
        printf("Usage: ./caesar <key>\n");
        return 1;
    }

    // 2. Parse the key and handle large integers (k % 26)
    int shift_value = atoi(argv[1]);

    // 3. Get input from the user
    string plaintext = get_string("Enter message to encrypt: ");

    // 4. Process and display the encrypted output
    printf("ciphertext: ");
    for (int i = 0, length = strlen(plaintext); i < length; i++)
    {
        char encrypted_char = shift_character(plaintext[i], shift_value);
        printf("%c", encrypted_char);
    }

    printf("\n");
    return 0;
}

/**
 * Checks if the user-provided string consists only of digits.
 * This prevents crashes or unexpected behavior from non-numeric keys.
 */
bool is_valid_numeric_key(string input)
{
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            return false;
        }
    }
    return true;
}

/**
 * Shifts a single character by 'k' positions.
 * Maintains alphabetical case and ignores punctuation/spaces.
 */
char shift_character(char c, int k)
{
    // The Caesar Cipher formula: (Position + Shift) % 26

    if (isupper(c))
    {
        return (c - 'A' + k) % 26 + 'A';
    }

    if (islower(c))
    {
        return (c - 'a' + k) % 26 + 'a';
    }

    // If it's a space, number, or symbol, return it as-is
    return c;
}
