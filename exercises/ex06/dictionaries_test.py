"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730234891"


def test_invert_one() -> None:
    """Test empty Invert."""
    test_invert: dict[str, str] = {}
    assert invert(test_invert) == {}


def test_invert_two() -> None:
    """Test for invert_two."""
    test_invert: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_invert) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_three() -> None: 
    """Test for invert three."""
    test_invert: dict[str, str] = {'Apple': 'Not Apple'}
    assert invert(test_invert) == {'Not Apple': 'Apple'}


def test_favorite_color_one() -> None: 
    """Test for favorite color one."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_two() -> None:
    """Test for favorite color two."""
    test_dict: dict[str, str] = {"Victor": "Orange"}
    assert favorite_color(test_dict) == "Orange"


def test_favorite_color_three() -> None: 
    """Test for favorite color three."""
    test_dict: dict[str, str] = {"Victor": "Orange", "Emma": "Blue"}
    assert favorite_color(test_dict) == "Orange"


def test_count_one() -> None:
    """Test for empty count one."""
    test_str: list[str] = ["Emma"]
    assert count(test_str) == {'Emma': 1}


def test_count_two() -> None: 
    """Test for count two."""
    test_str: list[str] = ["Victor", "Eunice", "Emma"]
    assert count(test_str) == {'Victor': 1, 'Eunice': 1, 'Emma': 1}


def test_count_three() -> None: 
    """Test for count three."""
    test_str: list[str] = ["Eunice", "Emma", "Eunice"]
    assert count(test_str) == {'Eunice': 2, 'Emma': 1}