Week 1: C Basics
This directory contains my solutions for the Problem Set 1 of Harvard's CS50 Introduction to Computer Science. These projects focus on the fundamental building blocks of C, including data types, conditional logic, loops, and custom functions.

Projects Overview
1. Hello
A simple introductory program that demonstrates basic input and output in C.

Key Concept: Using the get_string function from the cs50.h library to capture user input and formatting strings for output.

Source: hello.c

2. Mario (Less Comfortable)
A program that recreates the iconic Mario pyramid in the terminal using hashes (#).

Key Concept: Nested loops and right-alignment logic.

Logic: The program calculates the number of spaces needed per row using the formula height - current_row to ensure the pyramid is right-aligned.

Source: mario.c

3. Credit
A more complex program that determines the validity of a credit card number and identifies the card issuer (AMEX, MasterCard, or VISA).

Key Concept: Implementation of Luhn’s Algorithm (checksum) and handling long data types.

Logic: * Iterates through each digit of the card number.

Multiplies every other digit by 2 (starting from the second-to-last) and adds the products' digits together.

Adds the sum of the digits that weren't multiplied by 2.

Checks if the final total ends in 0 and verifies card length and starting prefixes.

Source: credit.c

How to Compile and Run
To run these programs locally, ensure you have the cs50 library installed. Use the following commands in your terminal:

Navigate to the directory:

Bash
cd "Week 1"
Compile the code:

Bash
make hello
make mario
make credit
Execute the program:

Bash
./mario

Learning Outcomes
Mastered terminal-based input/output.
Developed a deeper understanding of integer division and the modulo operator (%) for digit manipulation.
Practiced creating reusable code using custom functions (as seen in print_row in mario.c).

Practiced creating reusable code using custom functions (as seen in print_row in mario.c).
