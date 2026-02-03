import pytest

from sigma_pre_work.maxmin import maxmin, parse_numbers


def test_parse_numbers_valid_input() -> None:
    """Test parsing of a valid input string."""
    assert parse_numbers("10, 20, -30") == [10, 20, -30]
    assert parse_numbers("5;-15;25") == [5, -15, 25]
    assert parse_numbers("1:2:3") == [1, 2, 3]
    assert parse_numbers("  7 , 8 ; 9 : -10 ") == [7, 8, 9, -10]


def test_parse_numbers_invalid_input() -> None:
    """Test parsing of an invalid input string."""
    with pytest.raises(ValueError, match="Invalid input. Please enter integers only."):
        parse_numbers("10, twenty, 30")


def test_maxmin() -> None:
    """Test maxmin function."""
    assert maxmin([10, 20, -30, 5]) == [20, -30]
    assert maxmin([-1, -5, -3]) == [-1, -5]
    assert maxmin([0, 0, 0]) == [0, 0]
