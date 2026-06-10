import sys
import time
from datetime import datetime
from cs50 import SQL

# Initialize the SQLite database
db = SQL("sqlite:///honeypot.db")
db.execute("PRAGMA foreign_keys = ON;")

# Create tables
db.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TEXT NOT NULL,
        ai_verdict TEXT DEFAULT 'Unknown',
        threat_score REAL DEFAULT 0.0
    )
""")

db.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        timestamp TEXT NOT NULL,
        command TEXT NOT NULL,
        time_taken REAL NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions(session_id)
    )
""")

def calculate_running_score(session_id):
    """Queries current logs to find the real-time threat score"""
    logs = db.execute("SELECT command FROM logs WHERE session_id = ?", session_id)
    score = 0
    for log in logs:
        cmd = log["command"]
        if "sudo" in cmd: score += 50
        elif "passwords.txt" in cmd or "vault" in cmd: score += 40
        elif cmd in ["whoami", "uname"]: score += 15
        else: score += 5
    return min(score, 100.0)

def analyze_session(session_id):
    """Final session wrap-up and definitive verdict storage"""
    logs = db.execute("SELECT command, time_taken FROM logs WHERE session_id = ?", session_id)
    if not logs: return

    final_score = calculate_running_score(session_id)
    total_time = sum(log["time_taken"] for log in logs)
    avg_speed = total_time / len(logs)

    verdict = "Bot (Automated Threat)" if avg_speed < 1.0 else "Human (Targeted Threat)"

    db.execute("""
        UPDATE sessions SET ai_verdict = ?, threat_score = ? WHERE session_id = ?
    """, verdict, final_score, session_id)

    print("\n--- [AI ENGINE SESSION SUMMARY] ---")
    print(f"Assigned Session ID : {session_id}")
    print(f"Calculated Risk Score: {final_score}/100.0")
    print(f"Behavioral Verdict   : {verdict}")
    print("-----------------------------------\n")

def display_analyst_dashboard():
    """Fetches and displays historical honeypot records from the DB"""
    print("\n============================================================")
    print("      SIEM & CYBERSECURITY ANALYST THREAT DASHBOARD         ")
    print("============================================================\n")

    sessions = db.execute("SELECT * FROM sessions ORDER BY session_id DESC")

    if not sessions:
        print("[-] No tracking sessions recorded yet inside the database.")
        return

    for sess in sessions:
        sid = sess["session_id"]
        print(f"[+] SESSION #{sid} | Started: {sess['start_time']}")
        print(f"    AI Behavioral Verdict: {sess['ai_verdict']}")
        print(f"    Assessed Threat Score: {sess['threat_score']}/100.0")
        print("    Executed Operations:")

        logs = db.execute("SELECT timestamp, command, time_taken FROM logs WHERE session_id = ?", sid)
        for log in logs:
            print(f"      - [{log['timestamp']}] {log['command']} (Delay: {log['time_taken']:.2f}s)")
        print("-" * 60)

def main():
    # Analyst Mode routing check
    if len(sys.argv) > 1 and sys.argv[1] == "--analyst":
        display_analyst_dashboard()
        return

    current_dir = "/home/admin"
    username = "user"
    hostname = "ubuntu-server"

    start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session_id = db.execute("INSERT INTO sessions (start_time) VALUES (?)", start_time_str)

    print("Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-40-generic x86_64)")
    print("Last login: Mon Jun  8 14:22:01 2026 from 192.168.1.15")

    try:
        while True:
            prompt = f"{username}@{hostname}:{current_dir}$ "

            start_time = time.time()
            user_input = input(prompt).strip()
            end_time = time.time()

            if not user_input: continue

            typing_duration = end_time - start_time
            current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            db.execute("""
                INSERT INTO logs (session_id, timestamp, command, time_taken) VALUES (?, ?, ?, ?)
            """, session_id, current_timestamp, user_input, typing_duration)

            # Check risk level before rendering output
            running_score = calculate_running_score(session_id)

            current_dir = handle_command(user_input, current_dir, running_score)

    except (KeyboardInterrupt, EOFError):
        analyze_session(session_id)
        print("Connection closed by foreign host.")
        sys.exit(0)

def handle_command(user_input, current_dir, running_score):
    parts = user_input.split()
    cmd = parts[0]
    args = parts[1:] if len(parts) > 1 else []

    # 🚨 DECEPTION TRIGGER: Slow down high-threat attackers
    if running_score >= 40:
        time.sleep(1.5)

    if cmd == "exit":
        raise KeyboardInterrupt
    elif cmd == "clear":
        print("\033[H\033[J", end="")
    elif cmd == "pwd":
        print(current_dir)
    elif cmd == "whoami":
        print("user")
    elif cmd == "ls":
        if current_dir == "/home/admin":
            # 🚨 DECEPTION TRIGGER: Seduce high-threat attackers into a deep fake trap file
            if running_score >= 40:
                print("notes.txt    passwords.txt    bank_transfer_vault.env")
            else:
                print("notes.txt    passwords.txt")
        else:
            print("")
    elif cmd == "cat":
        if not args:
            print("cat: missing file operand")
        elif args[0] == "passwords.txt" and current_dir == "/home/admin":
            print("admin:P@ssword123\nroot:Secur3Str0ng!")
        elif args[0] == "notes.txt" and current_dir == "/home/admin":
            print("Reminder: Fix the vulnerability in the main firewall database.")
        elif args[0] == "bank_transfer_vault.env" and running_score >= 40:
            print("Error: Resource temporarily unavailable. Connection payload encrypted.")
        else:
            print(f"cat: {args[0]}: No such file or directory")
    elif cmd == "uname":
        print("Linux ubuntu-server 6.8.0-40-generic #40-Ubuntu SMP PREEMPT_DYNAMIC x86_64 GNU/Linux")
    elif cmd == "sudo":
        print("user is not in the sudoers file. This incident will be reported.")
    else:
        print(f"{cmd}: command not found")

    return current_dir

# 🚨 THE TRIGGER BLOCK: MUST BE FLUSH LEFT AT THE ABSOLUTE BOTTOM
if __name__ == "__main__":
    main()
