import csv
import sys


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py database sequence")
        sys.exit(1)

    # Read the CSV database into memory
    people = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        strs = reader.fieldnames[1:]  # All column names except "name"
        for row in reader:
            people.append(row)

    # Read the DNA sequence into memory
    with open(sys.argv[2]) as seqfile:
        sequence = seqfile.read()

    # Compute longest match for each STR in the DNA sequence
    counts = {str_seq: longest_match(sequence, str_seq) for str_seq in strs}

    # Check against each person in the database
    for person in people:
        if all(int(person[str_seq]) == counts[str_seq] for str_seq in strs):
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest = 0
    length = len(subsequence)

    for i in range(len(sequence)):
        count = 0
        while sequence[i + count * length : i + (count + 1) * length] == subsequence:
            count += 1
        longest = max(longest, count)

    return longest


main()
