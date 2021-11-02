"""Utility functions."""

__author__ = "730234891"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read in a table the rows of a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file.
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare a csv file to read the data file rather than just strings.
    csv_reader = DictReader(file_handle)

    # Begin to read each row of the CSV file, line by line. 
    for row in csv_reader: 
        result.append(row)

    # In need of resources, close the file when we're done.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Make a column-oriented table from a row-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result


def head(a: dict[str, list[str]], b: int) -> dict[str, list[str]]:
    """Return a coilum with a select number of rows."""
    if b > len(a): 
        b = len(a)
    result: dict[str, list[str]] = {}
    for d in a:
        i: int = 0 
        values: list[str] = []
        while i < b: 
            values.append(a[d][i])
            i += 1 
        result[d] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a subset of the original columns."""
    result: dict[str, list[str]] = {}
    for v in names:
        result[v] = table[v]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Make a two column table into one."""
    result: dict[str, list[str]] = {}
    for c in x:
        result[c] = x[c]
    for d in y:
        if d in x:
            i: int = 0
            while i < len(y[d]):
                x[d].append(y[d][i])
                i += 1
            result[d] = x[d]
        else:
            result[d] = y[d]
    return result
    

def count(list: list[str]) -> dict[str, int]: 
    """Count the number of times a number makes in a list."""
    result: dict[str, int] = {}
    i: int = 0 
    while i < len(list): 
        if list[i] in result: 
            result[list[i]] += 1
        else: 
            result[list[i]] = 1 
        i += 1 
    return result