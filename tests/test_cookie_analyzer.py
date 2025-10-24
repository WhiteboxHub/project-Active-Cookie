import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cookie_analyzer import get_most_active_cookies

def test_single_most_active_cookie():
    records = [
        ("A", "2018-12-09"),
        ("B", "2018-12-09"),
        ("A", "2018-12-09"),
        ("C", "2018-12-08"),
    ]
    result = get_most_active_cookies(records, "2018-12-09")
    assert result == ["A"]

def test_multiple_most_active_cookies():
    records = [
        ("A", "2018-12-09"),
        ("B", "2018-12-09"),
        ("A", "2018-12-09"),
        ("B", "2018-12-09"),
    ]
    result = sorted(get_most_active_cookies(records, "2018-12-09"))
    assert result == ["A", "B"]

def test_no_cookies_for_date():
    records = [
        ("A", "2018-12-08"),
        ("B", "2018-12-08"),
    ]
    result = get_most_active_cookies(records, "2018-12-09")
    assert result == []

@pytest.mark.parametrize("records,target_date,expected", [
    ([("A", "2018-12-09"), ("A", "2018-12-09"), ("B", "2018-12-08")],
     "2018-12-09", ["A"]),
    ([("X", "2020-01-01"), ("Y", "2020-01-01"), ("X", "2020-01-01"), ("Y", "2020-01-01")],
     "2020-01-01", ["X", "Y"]),
    ([("Z", "2021-05-05")],
     "2021-05-06", []),
])
def test_parametrized_cases(records, target_date, expected):
    assert sorted(get_most_active_cookies(records, target_date)) == sorted(expected)
