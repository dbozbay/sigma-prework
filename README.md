# Sigma Labs Pre-Course

A collection of programming exercises completed as part of the Sigma Labs pre-course program, implemented in both Python and Rust.

## Project Structure

```
.
├── python/              # Python project (managed with uv)
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── age.py
│   └── maxmin.py
└── rust/                # Rust project (managed with Cargo)
    ├── Cargo.toml
    └── src/
        ├── maxmin.rs
        └── age.rs
```

## Exercises

### 1. Maximum and Minimum Finder

Prompts the user to enter a list of integers and returns the highest and lowest numbers without using built-in max/min functions.

**Python Usage:**
```bash
cd python
uv run maxmin.py
```

**Python Example:**
```
Enter a list of integers separated by commas: 2, 4, 1, 0, 2, -1
Maximum and minimum values are: [4, -1]
```

**Rust Usage:**
```bash
cd rust
cargo run --bin maxmin
```

**Rust Example:**
```
Enter a list of integers separated by commas: -100, 0, 0, 0, 100
Maximum and minimum values are: [100, -100]
```

### 2. Age Calculator

Asks the user for their date of birth and calculates their current age.

**Python Usage:**
```bash
cd python
uv run age.py
```

**Python Example:**
```
Enter your date of birth (YYYY-MM-DD): 1995-06-15
You are 29 years old.
```

**Rust Usage:**
```bash
cd rust
cargo run --bin age
```

**Rust Example:**
```
Enter your date of birth (YYYY-MM-DD): 1995-06-15
You are 29 years old.
```

## Requirements

**Python:**
- Python 3.14 or higher
- `uv` package manager

**Rust:**
- Rust 1.70 or higher
- Cargo (included with Rust)

## Installation

**Python with uv:**
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to python directory
cd python

# uv will automatically manage the Python version, dependencies and virtual env with the `run` command
```

**Rust:**
```bash
# Install Rust from rustup.rs
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## License

This project is for educational purposes.