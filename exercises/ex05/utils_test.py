"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730234891"


def test_only_evens_empty() -> None: 
    """Testing the empty edge case for test_only."""
    list_1: list[int] = []
    assert only_evens(list_1) == []


def test_only_evens_single_item() -> None: 
    """Testing a single item for only_evens."""
    list_1: list[int] = [120]
    assert only_evens(list_1) == [120]


def test_only_evens_multiple_items() -> None: 
    """Testing multiple items for only_evens."""
    list_1: list[int] = [30, 35, 40, 45, 50, 55]
    assert only_evens(list_1) == [30, 40, 50]


def test_sub_empty() -> None:
    """Testing the empty edge case for test_sub."""
    list_1: list[int] = []
    assert sub(list_1, 0, 0) == []


def test_sub_single_items() -> None: 
    """Testing a single item for test_sub."""
    list_1: list[int] = [120]
    assert sub(list_1, 0, 1) == [120]


def test_sub_multiple_items() -> None: 
    """Testing multiple items for test_sub."""
    list_1: list[int] = [1, 2, 3]
    assert sub(list_1, 1, 3) == [2, 3]


def test_concat_empty() -> None: 
    """Testing the empty edge case for test_concat."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_single_item() -> None: 
    """Testing a single item for test_concat."""
    list_1: list[int] = [120]
    list_2: list[int] = [10]
    assert concat(list_1, list_2) == [120, 10]


def test_concat_multiple_items() -> None: 
    """Testing multiple items for test_concat."""
    list_1: list[int] = [30, 40, 50]
    list_2: list[int] = [60, 70, 80]
    assert concat(list_1, list_2) == [30, 40, 50, 60, 70, 80]