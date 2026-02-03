def get_user_input() -> str:
    """Prompt user for a list of integers separated by commas."""
    return input("Enter a list of integers: ").strip()


def parse_numbers(input: str, seperators: list[str] = [",", ";", ":"]) -> list[int]:
    """Parse a string into a list of integers based on given separators."""
    for sep in seperators:
        input = input.replace(sep, " ")

    try:
        result = [int(num) for num in input.split()]
    except ValueError as e:
        raise ValueError("invalid digit found in string") from e

    return result


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
        input = get_user_input()
        try:
            numbers = parse_numbers(input)
            if len(numbers) < 2:
                print("Please enter at least two integers.")
                continue
            print(f"Maximum and minimum values are: {maxmin(numbers)}")
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
