def get_user_numbers() -> list[int]:
    """Prompt user for a list of integers separated by commas."""
    numbers_input = input("Enter a list of integers: ")
    numbers = parse_numbers(numbers_input)

    if len(numbers) < 2:
        raise ValueError("Invalid input. Please enter at least two integers.")

    return parse_numbers(numbers_input)


def parse_numbers(numbers: str, seperators: list[str] = [",", ";", ":"]) -> list[int]:
    """Parse a string into a list of integers based on given separators."""
    normalized = numbers.strip()
    for sep in seperators:
        normalized = normalized.replace(sep, " ")

    try:
        normalized = [int(num) for num in normalized.split()]
    except ValueError as e:
        raise ValueError("Invalid input. Please enter integers only.") from e

    return normalized


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
    while True:
        try:
            numbers = get_user_numbers()
            result = maxmin(numbers)
            print(f"Maximum and minimum values are: {result}")
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
