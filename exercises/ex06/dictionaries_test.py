"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def invert_one() -> None:
    """Test empty Invert."""
    test_invert: dict[str, str] = {'Will': 'Victor', 'Emma': 'Phoebe'}
    assert invert(test_invert) == KeyError


def invert_two() -> None:
    """Test for invert_one."""
    test_invert: dict[str, str] = {'a': 'x', 'b': 'y', 'c': 'z'}
    assert invert(test_invert) == {'x': 'a', 'y': 'b', 'z': 'c'}


def invert_three() -> None: 
    """Test for invert 2."""
    test_invert: dict[str, str] = {'Nigeria': 'France'}
    assert invert(test_invert) == {'France': 'Nigeria'}


def favorite_color_one() -> None: 
    """Test for favorite color one."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def favorite_color_two() -> None:
    """Test for favorite color two."""
    test_dict: dict[str, str] = {"Victor": "Orange"}
    assert favorite_color(test_dict) == "Orange"


def favorite_color_three() -> None: 
    """Test for favorite color three."""
    test_dict: dict[str, str] = {"Victor": "Orange", "Emma": "Blue"}
    assert favorite_color(test_dict) == "Orange"


def count_one() -> None:
    """Test for empty count one."""
    test_str: list[str] = ['Evelyn', 'Eunice', 'Emma']
    assert count(test_str) == ["Emma: 2, Eunice: 1"]


def count_two() -> None: 
    """Test for count two."""
    test_str: list[str] = ['Victor', 'Eunice', 'Emma']
    assert count(test_str) == ["Victor: 1, Eunice: 1, Emma: 1"]


def count_three() -> None: 
    """Test for count three."""
    test_str: list[str] = ['Eunice', 'Emma', 'Eunice']
    assert count(test_str) == ["Eunice; 2, Emma: 1"]