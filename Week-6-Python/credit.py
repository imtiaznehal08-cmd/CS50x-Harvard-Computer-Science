from cs50 import get_int


def main():
    number = get_number()
    print(get_card_type(number))


def get_number():
    while True:
        n = get_int("Number: ")
        if n > 0:
            return n


def luhn_check(number):
    digits = [int(d) for d in str(number)]
    total = 0
    # Every second digit from the right, starting with the second-to-last
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled // 10 + doubled % 10
        else:
            total += digit
    return total % 10 == 0


def get_card_type(number):
    s = str(number)
    length = len(s)
    first_two = int(s[:2])
    first_one = int(s[0])

    if not luhn_check(number):
        return "INVALID"

    # AMEX: 15 digits, starts with 34 or 37
    if length == 15 and first_two in [34, 37]:
        return "AMEX"

    # MASTERCARD: 16 digits, starts with 51–55
    if length == 16 and 51 <= first_two <= 55:
        return "MASTERCARD"

    # VISA: 13 or 16 digits, starts with 4
    if length in [13, 16] and first_one == 4:
        return "VISA"

    return "INVALID"


main()
