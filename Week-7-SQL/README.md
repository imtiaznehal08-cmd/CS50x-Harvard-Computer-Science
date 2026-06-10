# CS50x - Week 7: SQL

This repository contains my solutions for the problem sets in **Week 7 (SQL)** of Harvard's CS50x introduction to computer science. This week's focus was on relational databases, learning how to write efficient queries, join multiple tables, and optimize data retrieval using SQLite.

## 📋 Projects Overview

1. **Fiftyville**: A complex, multi-table mystery-solving challenge where I tracked down a thief, an accomplice, and the escape city using database forensics.
2. **Movies**: A series of SQL queries designed to fetch, filter, and sort specific movie and actor data from an IMDb-style database.
3. **Songs**: A set of SQL queries used to analyze a Spotify-like database containing tracks, artists, and features like danceability or energy.

---

## 🕵️‍♂️ 1. Fiftyville (The Mystery of the CS50 Duck)

### The Case
The beloved CS50 duck was stolen from Humphrey Street on **July 28, 2025** at **10:15 AM**. The goal was to write SQL queries to cross-examine security logs, ATM transactions, phone records, and flight manifests to crack the case.

### Forensic Investigation Steps
* **Step 1:** Retrieved the crime scene report to establish the time (10:15 AM) and find witnesses.
* **Step 2:** Analyzed witness interviews (Ruth, Eugene, and Raymond) to gather critical clues.
* **Step 3 (The Parking Lot):** Checked bakery security logs for cars exiting between 10:15 AM and 10:25 AM.
* **Step 4 (The ATM):** Identified everyone who made an ATM withdrawal on Leggett Street earlier that morning.
* **Step 5 (The Phone Call):** Isolated individuals who made a phone call lasting under 1 minute while leaving the bakery.
* **Step 6 (The Suspect Intersection):** Intersected the license plates, ATM records, and callers to narrow the suspects down to **Bruce** and **Diana**.
* **Step 7 & 8 (The Flight):** Found the earliest flight leaving Fiftyville the next morning (July 29) to **New York City** and discovered **Bruce** was on it.
* **Step 9 (The Accomplice):** Tracked the recipient of Bruce's short phone call to identify the accomplice.

### Case Resolution
* **The Thief:** Bruce
* **The Accomplice:** Robin
* **The City Escaped To:** New York City

> See the full investigative process and queries in [`log.sql`](./log.sql).

---

## 🎬 2. Movies

This project involves writing SQL queries to answer specific questions using an IMDb-like database containing `movies`, `people`, `stars`, `directors`, and `ratings`.

### Sample Queries Written:
* **`1.sql`**: List the titles of all movies released in 2008.
* **`2.sql`**: Find the birth year of Emma Stone.
* **`3.sql`**: List all movies released since 2018 in alphabetical order.
* **`4.sql`**: Count the number of movies with a perfect 10.0 rating.
* **`5.sql`**: Find all Harry Potter movies, sorted chronologically.
* **`6.sql`**: Calculate the average rating of all movies released in 2012.
* **`7.sql`**: List all 2010 movies and their ratings, ordered by rating (highest to lowest).
* **`8.sql`**: List the names of all people who starred in *Toy Story*.

> All 13 relational queries are located in files `1.sql` through `13.sql`.

---

## 🎵 3. Songs

This section utilizes a database containing information from Spotify about songs and their audio attributes (energy, valence, tempo, danceability, etc.).

### SQL Queries Cover:
* Listing names of all songs in the database.
* Sorting songs by their tempo or duration.
* Finding the average energy of songs by specific parameters.
* Identifying top-performing artists based on song attributes.
* Analyzing attributes like "danceability" to find the most upbeat tracks.

---

## 🛠️ How to Run

To run these queries locally, make sure you have `sqlite3` installed.

1. **For Fiftyville:**
   
   sqlite3 fiftyville.db < log.sql

2. **For Movies:**

sqlite3 movies.db < 1.sql

3. **For Songs:**

sqlite3 songs.db < 1.sql

**🧠 Key Skills Learned**
Writing complex SELECT queries utilizing WHERE, ORDER BY, GROUP BY, and LIMIT.
Mastering table normalization and optimizing data relationships using JOIN (Inner, Left/Right).
Utilizing subqueries (IN, EXISTS) and nested queries to narrow down targeted datasets.
Applying aggregate functions like COUNT(), AVG(), SUM(), and MIN()/MAX().
