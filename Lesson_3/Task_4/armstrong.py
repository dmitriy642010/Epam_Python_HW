def is_armstrong(number: int) -> bool:
    digits = [int(d) for d in str(number)]
    length = len(digits)
    result = 0

    for digit in digits:
        result += digit ** length

    return result == number
