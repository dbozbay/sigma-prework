from datetime import datetime


def get_user_dob() -> datetime:
    """Prompt user for a valid date of birth in YYYY-MM-DD format."""
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        return datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD format.")


def calculate_age(dob: datetime) -> int:
    """Calculate age based on date of birth."""
    today = datetime.today()

    if dob > today:
        raise ValueError("Invalid date of birth. Cannot be in the future.")

    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def main() -> None:
    while True:
        try:
            dob = get_user_dob()
            age = calculate_age(dob)
            print(f"You are {age} years old.")
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
