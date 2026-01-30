def get_valid_numbers() -> list[int]:
    """Prompt user for a list of integers separated by commas."""
    while True:
        try:
            numbers_input = input("Enter a list of integers separated by commas: ")
            numbers = [int(num.strip()) for num in numbers_input.split(",")]
            if len(numbers) < 2:
                print("Please enter at least two integers.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue


def maxmin(numbers: list[int]) -> list[int]:
    """Return the maximum and minimum values from a list of integers."""
    lowest = highest = numbers[0]

    for num in numbers[1:]:
        if num < lowest:
            lowest = num

        elif num > highest:
            highest = num

    return [highest, lowest]


def main() -> None:
    numbers = get_valid_numbers()
    result = maxmin(numbers)
    print(f"Maximum and minimum values are: {result}")


if __name__ == "__main__":
    main()
