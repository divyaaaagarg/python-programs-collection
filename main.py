"""Interactive launcher for the Python Programs Collection."""
from factorial import factorial
from fibonacci import fibonacci_sequence
from structure_to_dictionary import structure_to_dictionary


def main() -> None:
    while True:
        print("\n=== Python Programs Collection ===")
        print("1. Factorial")
        print("2. Fibonacci sequence")
        print("3. Structure to dictionary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == "1":
                number = int(input("Enter a non-negative integer: "))
                print(f"{number}! = {factorial(number)}")
            elif choice == "2":
                count = int(input("How many terms? "))
                print(fibonacci_sequence(count))
            elif choice == "3":
                fields = ["name", "course", "semester"]
                values = [
                    input("Name: ").strip(),
                    input("Course: ").strip(),
                    input("Semester: ").strip(),
                ]
                print(structure_to_dictionary(fields, values))
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Please choose a number from 1 to 4.")
        except ValueError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    main()
