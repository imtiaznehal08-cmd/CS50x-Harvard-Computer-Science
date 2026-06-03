# CS50x Week 6: Python

This repository contains my implementations for **Week 6** of Harvard University's **CS50x: Introduction to Computer Science**. 

After spending the first several weeks building a solid foundational understanding of low-level memory management, pointers, and data structures using C, Week 6 transitions into **Python**. These projects focus on writing cleaner, more abstract high-level code while solving identical or scaled-up algorithmic challenges from earlier weeks.

---

## 🚀 Projects Overview

Here is a breakdown of the Python scripts included in this directory:

### 1. Hello (`hello.py`)
A simple, classic warm-up program that prompts the user for their name using Python's built-in `input()` function and prints a personalized greeting. This highlights the simplicity of Python syntax compared to C's `stdio.h` boilerplates.

### 2. Mario (Less/More Comfortable) (`mario.py`)
An implementation that prints a double, adjacent pyramid of blocks (represented by `#`) of a user-specified height between 1 and 8. 
* Uses a `while True` loop to handle robust input validation.
* Leverages Python's powerful string multiplication (`" " * spaces`) to draw the pyramids cleanly without nested loops.

### 3. Credit (`credit.py`)
A script that prompts a user for a credit card number and uses **Luhn's Algorithm** to determine if the number is syntactically valid, along with identifying the issuer: **AMEX**, **MASTERCARD**, or **VISA**.
* **Key Features:** Built-in list comprehensions to isolate, reverse, and dynamically double alternating digits, followed by checking lengths and starting prefixes.

### 4. Readability (`readability.py`)
Calculates the approximate reading grade level of a body of text using the **Coleman-Liau index formula**:
$$index = 0.0588 \times L - 0.296 \times S - 15.8$$
* Where $L$ is the average number of letters per 100 words, and $S$ is the average number of sentences per 100 words.
* **Key Features:** Utilizes Python string methods and generator expressions (`isalpha()`, `.split()`, and punctuation filtering) to count metrics instantly.

### 5. DNA (`dna.py`)
A data-heavy command-line application that identifies a person based on a sample of their DNA sequence. 
* The program takes a CSV database containing Short Tandem Repeat (STR) counts for individuals and a text file containing a raw DNA sequence.
* It computes the longest consecutive run of each STR in the DNA sequence, maps those counts against the CSV data using `csv.DictReader`, and outputs the matching name (or "No match").

---

## 🛠️ Library Dependencies

Some files utilize the standard `cs50` Python package helper functions for input validation and explicit variable casting:
* `get_int()`
* `get_string()`

To install this helper library locally, run:
```bash
pip install cs50

🧠 **Key Takeaways from Week 6**
Syntax Efficiency: Learned how hundreds of lines of C logic involving memory allocations and string formatting can be gracefully executed in just a fraction of the lines using Python.

File & Data Manipulation: Developed experience handling raw string indexing, multi-conditioned structures, and parsing files with the native csv module.

Memory Management Realization: Gained insight into how interpreted languages automate garbage collection and type assignments behind the scenes, referencing the binary concepts mastered in earlier weeks.
