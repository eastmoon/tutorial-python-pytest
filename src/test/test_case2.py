#
from mymath import *

#
def test_string_1(order):
    # Assert
    assert order == ["a", 2]

#
def test_string_2(order, expected_list):
    # Act
    order.append(3.0)
    # Assert
    assert order == expected_list
