from cs50 import get_int

def main():
    height = get_height()
    print_pyramids(height)

def get_height():
    while True:
        n = get_int("Height: ")
        if 1 <= n <= 8:
            return n

def print_pyramids(height):
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        hashes = "#" * row
        print(f"{spaces}{hashes}  {hashes}")

main ()
