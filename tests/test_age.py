from datetime import datetime, timedelta

import pytest

from sigma_pre_work.age import calculate_age

today = datetime.today()


def test_age_with_birthday_today() -> None:
    """Test age calculation when birthday is today."""
    dob = datetime(today.year - 30, today.month, today.day)
    assert calculate_age(dob) == 30


def test_age_with_birthday_tomorrow() -> None:
    """Test age calculation when birthday is tomorrow."""
    tomorrow = today + timedelta(days=1)
    dob = datetime(tomorrow.year - 30, tomorrow.month, tomorrow.day)
    assert calculate_age(dob) == 29


def test_age_with_birthday_yesterday() -> None:
    """Test age calculation when birthday was yesterday."""
    yesterday = today - timedelta(days=1)
    dob = datetime(yesterday.year - 30, yesterday.month, yesterday.day)
    assert calculate_age(dob) == 30


def test_age_with_newborn() -> None:
    """Test age calculation for a newborn."""
    dob = today
    assert calculate_age(dob) == 0


def test_age_with_invalid_future_dob() -> None:
    """Test age calculation with a future date of birth."""
    with pytest.raises(ValueError, match="Invalid date of birth."):
        dob = datetime(today.year + 1, today.month, today.day)
        calculate_age(dob)
