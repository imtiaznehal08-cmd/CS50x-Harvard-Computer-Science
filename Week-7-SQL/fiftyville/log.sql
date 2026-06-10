-- Keep a log of any SQL queries you execute as you solve the mystery.
-- =========================================================
-- STEP 1: Find the crime scene report
-- The problem says theft was on July 28, 2025, Humphrey Street
-- =========================================================
SELECT *
  FROM crime_scene_reports
 WHERE year = 2025
   AND month = 7
   AND day = 28
   AND street = 'Humphrey Street';
-- Found report #295: Theft of the CS50 duck at 10:15am at the Humphrey Street bakery.
-- Three witnesses were interviewed; each transcript mentions the bakery.

-- =========================================================
-- STEP 2: Read the three witness interviews from that day
-- =========================================================
SELECT name, transcript
  FROM interviews
 WHERE year = 2025
   AND month = 7
   AND day = 28
   AND transcript LIKE '%bakery%';
-- Ruth:    Thief left bakery parking lot within 10 minutes of 10:15am -> exited by 10:25am
-- Eugene:  Thief was at the ATM on Leggett Street withdrawing money earlier that morning
-- Raymond: Thief made a phone call lasting under 1 minute while leaving; said they'd take
--          the EARLIEST flight out of Fiftyville TOMORROW (July 29), and asked the
--          receiver to purchase the ticket -- that receiver is the accomplice.

-- =========================================================
-- STEP 3 (Ruth's clue): Check bakery security logs
-- Who exited the parking lot between 10:15 and 10:25?
-- =========================================================
SELECT license_plate
  FROM bakery_security_logs
 WHERE year = 2025
   AND month = 7
   AND day = 28
   AND hour = 10
   AND minute BETWEEN 15 AND 25
   AND activity = 'exit';
-- 8 license plates: 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- =========================================================
-- STEP 4 (Eugene's clue): Who withdrew from Leggett St ATM on July 28?
-- =========================================================
SELECT p.name, p.phone_number, p.passport_number, p.license_plate
  FROM people p
  JOIN bank_accounts ba ON ba.person_id = p.id
  JOIN atm_transactions atm ON atm.account_number = ba.account_number
 WHERE atm.year = 2025
   AND atm.month = 7
   AND atm.day = 28
   AND atm.atm_location = 'Leggett Street'
   AND atm.transaction_type = 'withdraw';
-- 8 people: Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista

-- =========================================================
-- STEP 5 (Raymond's clue): Who made a phone call under 1 minute on July 28?
-- =========================================================
SELECT caller
  FROM phone_calls
 WHERE year = 2025
   AND month = 7
   AND day = 28
   AND duration < 60;
-- Several phone numbers returned

-- =========================================================
-- STEP 6: Intersect all three clues to find the suspects
-- Must match: (a) exit plate, (b) ATM withdrawal, (c) short phone call
-- =========================================================
SELECT p.name, p.phone_number, p.passport_number, p.license_plate
  FROM people p
  JOIN bank_accounts ba ON ba.person_id = p.id
  JOIN atm_transactions atm ON atm.account_number = ba.account_number
 WHERE atm.year = 2025
   AND atm.month = 7
   AND atm.day = 28
   AND atm.atm_location = 'Leggett Street'
   AND atm.transaction_type = 'withdraw'
   AND p.license_plate IN (
       SELECT license_plate
         FROM bakery_security_logs
        WHERE year = 2025
          AND month = 7
          AND day = 28
          AND hour = 10
          AND minute BETWEEN 15 AND 25
          AND activity = 'exit'
   )
   AND p.phone_number IN (
       SELECT caller
         FROM phone_calls
        WHERE year = 2025
          AND month = 7
          AND day = 28
          AND duration < 60
   );
-- Two suspects remain: Bruce (plate=94KL13X, phone=(367) 555-5533)
--                  and Diana (plate=322W7JE, phone=(770) 555-1861)

-- =========================================================
-- STEP 7: Find the earliest flight out of Fiftyville on July 29
-- =========================================================
SELECT f.id, f.hour, f.minute, dest.city AS destination
  FROM flights f
  JOIN airports orig ON orig.id = f.origin_airport_id
  JOIN airports dest ON dest.id = f.destination_airport_id
 WHERE f.year = 2025
   AND f.month = 7
   AND f.day = 29
   AND orig.city = 'Fiftyville'
 ORDER BY f.hour, f.minute;
-- Earliest is Flight #36 at 08:20 -> New York City

-- =========================================================
-- STEP 8: Check which suspect is on the earliest flight
-- =========================================================
SELECT p.name, pa.seat
  FROM passengers pa
  JOIN people p ON p.passport_number = pa.passport_number
 WHERE pa.flight_id = 36
   AND p.name IN ('Bruce', 'Diana');
-- Result: Bruce is on flight 36, seat 4A. Diana is NOT.
-- THIEF = BRUCE, escaped to NEW YORK CITY

-- =========================================================
-- STEP 9: Find the accomplice -- who received Bruce's short call?
-- =========================================================
SELECT p.name, p.phone_number
  FROM people p
 WHERE p.phone_number = (
     SELECT receiver
       FROM phone_calls
      WHERE caller = '(367) 555-5533'
        AND year = 2025
        AND month = 7
        AND day = 28
        AND duration < 60
 );
-- Result: Robin -- the accomplice who purchased Bruce's flight ticket

-- =========================================================
-- CONCLUSION
-- Thief:      Bruce
-- Escaped to: New York City
-- Accomplice: Robin
-- =========================================================

