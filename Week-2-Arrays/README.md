# Week 2: Arrays

This directory contains my solutions for the **Week 2** problem sets of Harvard's **CS50x: Introduction to Computer Science**. These projects focus on how data is stored in memory using arrays, string manipulation, and the implementation of cryptographic algorithms.

### 🛠 Skills Demonstrated
* **Mathematics:** ASCII arithmetic, modular mapping (modulo 26), and linguistic indexing formulas.
* **Logic:** Iterating through strings, character-to-integer conversion, and case-preservation logic.
* **Tooling:** Command-line argument parsing and multi-library integration (`ctype.h`, `math.h`, `string.h`).

---

### Projects Overview

#### **Scrabble**
A program that determines the winner of a Scrabble game by calculating the point values of two words.
* **Key Concept:** Using a static integer array to map alphabetical characters to specific point values.
* **Logic:** The program subtracts 'A' or 'a' from a character to find its index (0–25) in a `POINTS` array, then sums those values to compare player scores.
* **Source:** `scrabble.c`

#### **Readability**
An implementation of the **Coleman-Liau index** to estimate the US grade level required to read a text.
* **Key Concept:** Text analysis through counting discrete linguistic units.
* **Logic:** It uses the formula `index = 0.0588 * L - 0.296 * S - 15.8`, where `L` is letters per 100 words and `S` is sentences per 100 words. It handles edge cases like "Before Grade 1" or "Grade 16+".
* **Source:** `readability.c`

#### **Caesar**
A program that encrypts messages using a Caesar cipher, shifting each letter by a user-defined key.
* **Key Concept:** Parsing command-line arguments and maintaining data integrity during transformation.
* **Logic:** The program validates that the user provided a numeric key via `argv[1]`, converts it to an integer, and uses modular arithmetic to wrap alphabetical shifts while keeping symbols and spaces unchanged.
* **Source:** `caesar.c`

---

### How to Compile and Run
To run these programs, ensure you have the `cs50` library installed. Use these commands in your terminal:

**1. Compile the code:**
```bash
make scrabble
make readability
make caesar
```

**2. Execute the programs:**
```bash
./scrabble
./readability
./caesar 13
```

### Learning Outcomes
* Mastered **array indexing** to store and retrieve data efficiently.
* Developed a deep understanding of **string manipulation**, recognizing that strings are simply arrays of characters ending in a null terminator.
* Practiced **input validation** by ensuring command-line arguments meet specific criteria before execution.