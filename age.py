from datetime import datetime


def get_valid_date_of_birth() -> datetime:
    """Prompt user for a valid date of birth in YYYY-MM-DD format."""
    while True:
        try:
            date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Date of birth must be in YYYY-MM-DD format.")
            continue


def calculuate_age(dob: datetime) -> int:
    """Calculate age based on date of birth."""
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


def main() -> None:
    dob = get_valid_date_of_birth()
    age = calculuate_age(dob)
    print(f"You are {age} years old.")


if __name__ == "__main__":
    main()
