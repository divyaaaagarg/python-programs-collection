"""Calculate the factorial of a non-negative integer."""

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is defined here only for non-negative integers.")
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


if __name__ == "__main__":
    try:
        value = int(input("Enter a non-negative integer: "))
        print(f"{value}! = {factorial(value)}")
    except ValueError as error:
        print(f"Invalid input: {error}")
