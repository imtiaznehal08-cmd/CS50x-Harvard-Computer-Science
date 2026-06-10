# AI-Driven Behavioral Honeypot & Adaptive Sandbox

#### Video Demo: https://youtu.be/I84GfJHM_Pg

#### Description:
This project is an advanced, terminal-based AI Behavioral Honeypot and Adaptive Sandbox developed as the final capstone project for CS50x. Built entirely in Python and backed by a relational SQLite database via the CS50 SQL library, this application provides an interactive environment engineered to detect, profile, and neutralize malicious network operators in real-time using behavioral analytics and active deception.

Traditional defensive honeypots are typically static: they emulate a vulnerable service, log incoming keystrokes to a flat-file repository, and offer no dynamic resistance. This architecture introduces a **Dynamic Deception Engine** that actively scales a running session risk index based on the context of executed terminal commands. Once an intruder crosses a defined threat threshold, the sandbox modifies its environmental state dynamically—injecting high-value deep-fake assets to distract the adversary and introducing artificial command-line latency to stall automated enumeration.

Additionally, the program features a **Behavioral AI Engine** that captures precise typing telemetry. By analyzing the intervals between executed operations, it mathematically distinguishes between fast, automated scripts (bots) and deliberate human threat actors.

The application features a dual-mode interface: an authentic **Honeypot Linux Terminal** for trapping intruders and a secure **SIEM Analyst Dashboard** accessible via administrative runtime flags for historical forensics.

---

## Technical Features

1. **Realistic Shell Emulation (REPL):** Implements an interactive Read-Eval-Print Loop closely mimicking an Ubuntu 24.04.1 LTS environment. It handles directory context, multi-argument input routing, and custom command binaries without exposing actual underlying kernel resources to danger.
2. **Normalized Relational Backend:** Leverages SQLite to log activity across two normalized tables (`sessions` and `logs`) tied explicitly through a one-to-many relationship using foreign keys.
3. **Contextual Threat Heuristics:** Maps explicit input patterns to risk weights inspired by standard cybersecurity attack frameworks:
   - *Discovery & Reconnaissance* (`whoami`, `uname`): Low Threat (15 points)
   - *Targeted Credential Access* (`cat passwords.txt`): Medium Threat (40 points)
   - *Privilege Escalation Attempts* (`sudo`): High Threat (50 points)
4. **Adaptive Environmental State Shifting:** When the active threat score equals or exceeds `40`, the sandbox dynamically triggers two defense countermeasures:
   - *Deceptive Asset Injection:* Automatically appends a fake high-value container environment file (`bank_transfer_vault.env`) to mock outputs of the `ls` command.
   - *Rate-Limiting Latency:* Introduces a blocking `time.sleep(1.5)` penalty to subsequent commands to disrupt rapid-fire scanning.
5. **Keystroke Telemetry Analytics:** Measures the absolute delta time between consecutive command submissions, creating an analytical profile to categorize threats.
6. **SIEM Administrative Console:** Provides a robust command-line auditing module that queries historical database records to display session metadata, final risk scores, behavioral classifications, and sequential action lists with millisecond timing breakdowns.

---

## Relational Database Schema Design

The backend data collection relies on two cleanly normalized tables designed to maintain strict data integrity through relational foreign key constraints:

### 1. `sessions` Table (Parent)
Tracks the overarching metadata associated with a single network connection instance.
- `session_id`: INTEGER, Primary Key, Auto-incremented.
- `start_time`: TEXT, Records the exact date and timestamp when the shell loop was initialized.
- `ai_verdict`: TEXT, Stores the post-session behavioral assessment ("Human" vs. "Bot").
- `threat_score`: REAL, Holds the cumulative calculated risk metric capped at 100.0.

### 2. `logs` Table (Child)
Captures every individual payload executed within an active session.
- `id`: INTEGER, Primary Key, Auto-incremented.
- `session_id`: INTEGER, Foreign Key referencing `sessions(session_id)`.
- `timestamp`: TEXT, The exact time of command submission.
- `command`: TEXT, The raw input string typed by the user.
- `time_taken`: REAL, The exact duration in seconds spent preparing and executing the command.

---

## Core Algorithms & Mathematical Logic

### 1. Real-Time Cumulative Risk Indexing
For each string processed through the terminal parser, the system queries the active logging sequence and evaluates the threat weight. The mathematical formula used to determine the threat posture is defined as:

$$\text{Running Risk Score} = \min\left(\sum_{i=1}^{n} \text{Weight}(\text{Command}_i), \, 100.0\right)$$

### 2. Inter-Command Interval (ICI) Analytics
Upon session closure (triggered by typing `exit` or raising a `KeyboardInterrupt` via `Ctrl + C`), the Behavioral Engine compiles all captured timing vectors to calculate the mean operation delay:

$$\text{Average ICI} = \frac{\sum_{i=1}^{m} \text{TimeTaken}_i}{m}$$

$$\text{AI Behavioral Profile} = \begin{cases} \text{"Bot (Automated Threat)"}, & \text{if } \text{Average ICI} < 1.0\text{s} \\ \text{"Human (Targeted Threat)"}, & \text{if } \text{Average ICI} \ge 1.0\text{s} \end{cases}$$

---

## Critical Design Choices & Engineering Trade-offs

### Command Line Interface vs. Graphical Web Application
While building a Flask-based web dashboard or a graphical UI would offer standard visual appeal, a clean Command Line Interface (CLI) was selected for maximum alignment with real-world security scenarios. Legitimate automated attack scripts and remote hackers interact strictly over SSH text terminals. Building the honeypot directly into the shell environment preserves full authenticity for incoming connections, while focusing development entirely on relational data structuring, low-latency execution loops, and string parsing algorithms.

### Native Heuristic Scoring vs. Machine Learning Dependencies
Using heavy external frameworks (such as Scikit-Learn or TensorFlow) to perform behavioral profiling would inject massive library dependencies and memory bloat into the repository. Implementing native algorithmic scoring thresholds allows the tool to run lightning-fast calculations natively in pure Python, optimizing resource performance while presenting completely transparent, auditable code to the CS50 evaluation staff.

---

## Deployment & Operational Guide

### 1. Launching the Honeypot Environment
To deploy the active interactive trap and begin gathering network adversary intelligence, execute the main script from your workspace terminal:
```bash
python app.py

---

## AI Use Disclosure & Acknowledgments

In compliance with the CS50x Academic Honesty guidelines regarding generative AI, this project utilized AI assistance (Gemini) as a collaborative pair programmer.

### Scope of AI Assistance:
- **Architecture Design:** Assisted in designing the relational one-to-many schema logic between the `sessions` and `logs` tables.
- **Debugging & Error Resolution:** Provided code troubleshooting for handling the dynamic execution of terminal inputs and formatting the SQLite queries within the `cs50.SQL` structure.
- **Documentation:** Assisted in generating the structured formatting and technical terminology used throughout this `README.md` file.

All final implementation, environment logic loops, custom terminal routing, and verification tests were managed and executed entirely by the author.
