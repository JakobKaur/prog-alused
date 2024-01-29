"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False

def test__lottery__all_5__return_10():
    """If all numbers are 5, return 10."""
    assert lottery(5, 5, 5) == 10

def test__lottery__all_same_but_not_5__return_5():
    """If all numbers are the same but not 5, return 5."""
    assert lottery(2, 2, 2) == 5

def test__lottery__all_different__return_1():
    """If all numbers are different, return 1."""
    assert lottery(2, 3, 1) == 1

def test__lottery__one_same_as_another__return_0():
    """If one number is the same as another, return 0."""
    assert lottery(2, 3, 2) == 0

def test__fruit_order__not_enough_weight__return_minus_1():
    """If ordered weight cannot be fulfilled, return -1."""
    assert fruit_order(4, 1, 10) == -1

def test__fruit_order__enough_weight__return_correct_amount():
    """If ordered weight can be fulfilled, return correct amount of small baskets."""
    assert fruit_order(4, 1, 9) == 4
