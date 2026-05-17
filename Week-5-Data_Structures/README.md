Here is a complete, polished README.md template tailored for CS50x Week 5 (Data Structures). It maintains the same crisp, professional, and readable structure as your Week 4 documentation, highlighting the massive leap from memory management to complex data structures like linked lists, tries, and hash tables.

🏗️ CS50x Week 5: Data Structures
This repository contains my implementations for the Week 5 Problem Set, focusing on abstract data structures, dynamic memory management, pointer manipulation, and optimizing algorithmic runtime efficiency (O(1) vs. O(N)).

📂 Projects
🌳 Inheritance
Goal: Simulate the inheritance of blood types over three generations of a family.

Implementation: Utilizes a custom person struct containing pointers to two parent structs. Dynamically allocates memory for a family tree of a specified generation depth, assigns alleles randomly based on genetic inheritance rules, and recursively frees the memory to prevent leaks.

File: inheritance.c

🔤 Speller
Goal: Build the fastest possible spell-checker that loads a dictionary of words into memory and checks a text file for misspelled words.

Implementation: Implemented a spell-checker using a custom Hash Table (or Trie, depending on your choice) to minimize lookup time. Designed a deterministic hash function to map strings to buckets and handled collisions using separate chaining with linked lists.

Files: dictionary.c, dictionary.h

**📊 Algorithmic Efficiency & Data Structures**
This week transitioned from contiguous memory allocation (arrays) to node-based data structures, evaluating the trade-offs between time and space complexity:

Data Structure	Insertion Time	Search Time	Memory Overhead
Singly Linked List	O(1)	O(N)	Low (one pointer per node)
Hash Table (Chained)	O(1) average	O(1) average / O(N) worst-case	Medium (array of pointers + node pointers)
Trie (Retrieval Tree)	O(L) where L is word length	O(L) where L is word length	High (array of 27 pointers per node)

**🛠️ Usage**
Each program can be compiled and executed using the standard CS50 tools:

Compiling and Running Inheritance
**Bash**
make inheritance
./inheritance

Compiling and Running Speller
**Bash**
make speller
./speller dictionaries/large texts/lalaland.txt

**🔍 Memory Safety & Performance**
Data structures require complex pointer swapping, making memory safety paramount. All code has been optimized and thoroughly checked with Valgrind to ensure:

Complete Memory Reclamation: Every dynamically allocated node (malloc) in the linked lists/trie is properly traversed and freed at the end of execution.

No Memory Corruption: Orphaned pointers and dangling references are avoided during pointer restructuring.

Optimized Execution: Maximized performance in speller by reducing hash collisions and ensuring efficient check loops.

**🎓 Learning Outcomes**
By completing this week's challenges, I have mastered:

Custom Struct Design: Creating self-referential structures (nodes) capable of pointing to data of their own type.

Dynamic Data Restructuring: Prepending nodes to linked lists, traversing structures without losing the "head" pointer, and freeing nested nodes recursively or iteratively.

Hashing & Collision Resolution: Designing robust hash functions and building arrays of linked lists to create operational hash tables.

Algorithmic Profiling: Understanding the real-world performance differences between various data structures when handling large datasets.
