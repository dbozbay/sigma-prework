def get_user_numbers() -> list[int]:
    """Prompt user for a list of integers separated by commas."""
    try:
        numbers_input = input("Enter a list of integers separated by commas: ")
        numbers = [int(num.strip()) for num in numbers_input.split(",")]
    except ValueError:
        raise ValueError("Invalid input. Please enter integers only.")

    if len(numbers) < 2:
        raise ValueError("Invalid input. Please enter at least two integers.")

    return numbers


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
