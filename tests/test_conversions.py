import pytest
from converter import conversions


def test_valid_conversion():
    '''Returns multiple of the quanity'''
    quanity = 6
    froam = "tsp"
    to = "tbsp"

    expected = 2
    actual = conversions.convert(quanity, froam, to)
    assert actual == expected


def test_valid_reversed():
    '''Look up order for units does not matter'''
    quanity = 3
    froam = "tbsp"
    to = "tsp"

    expected = 9
    actual = conversions.convert(quanity, froam, to)
    assert actual == expected


def test_no_conversion():
    '''Two valid units that do not have a valid conversion'''
    quanity = 3
    froam = "tbsp"
    to = "mph"

    with pytest.raises(ValueError):
        conversions.convert(quanity, froam, to)


def test_unknown_unit():
    '''No conversions exist for one or more given inputs'''
    quanity = 3
    froam = "tbsp"
    to = "couch"

    with pytest.raises(ValueError):
        conversions.convert(quanity, froam, to)
