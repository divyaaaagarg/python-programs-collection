"""Generate the first n Fibonacci numbers."""

def fibonacci_sequence(count: int) -> list[int]:
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    try:
        count = int(input("How many Fibonacci numbers? "))
        print(fibonacci_sequence(count))
    except ValueError as error:
        print(f"Invalid input: {error}")
