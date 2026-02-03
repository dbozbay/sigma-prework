# Sigma Labs Pre-Course

A collection of programming exercises completed as part of the Sigma Labs pre-course program, implemented in Python.

## Requirements

- Python 3.14 or higher
- `uv` package manager (recommended)

## Installation

1. Install `uv` (will automatically manage the Python version, dependencies and virtual env with the `run` command):

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Clone this repository:

    ```bash
    git clone git@github.com:dbozbay/sigma-prework.git
    cd sigma-prework
    ```

3. The project is ready to use! `uv` will automatically handle dependencies when you run scripts or tests.

## Exercises

### 1. Maximum and Minimum Finder

Prompts the user to enter a list of integers and returns the highest and lowest numbers without using built-in max/min functions.

**Usage:**
```bash
# Preferred: using the defined script
uv run maxmin

# Alternative: using python directly
python src/sigma_pre_work/maxmin.py
```

**Example:**
```
Enter a list of integers: 2, 4, 1, 0, 2, -1
Maximum and minimum values are: [4, -1]
```

### 2. Age Calculator

Asks the user for their date of birth and calculates their current age.

**Usage:**
```bash
# Preferred: using the defined script
uv run age

# Alternative: using python directly
python src/sigma_pre_work/age.py
```

**Example:**
```
Enter your date of birth (YYYY-MM-DD): 1995-06-15
You are 29 years old.
```

## Testing

Run the test suite to verify all exercises work correctly:

```bash
# Run all tests
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_maxmin.py
uv run pytest tests/test_age.py
```

## License

This project is for educational purposes.
