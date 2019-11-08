from .first_recurring_char import first_recurring_char


def test_first_recurring_char_found():
    # Prepare
    s = "DBCABA"
    expected = "B"
    # Execute
    actual = first_recurring_char(s)
    # Assert
    assert actual == expected


def test_first_recurring_char_not_found():
    # Prepare
    s = "DBCA"
    expected = None
    # Execute
    actual = first_recurring_char(s)
    # Assert
    assert actual == expected


def test_first_recurring_char_found_min():
    # Prepare
    s = "AA"
    expected = "A"
    # Execute
    actual = first_recurring_char(s)
    # Assert
    assert actual == expected
