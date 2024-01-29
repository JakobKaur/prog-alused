"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if 18 <= time <= 24:
        return False
    elif 5 <= time <= 17:
        return coffee_needed
    else:
        return False



def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == b == c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b != c != a:
        return 1
    elif a == b or b == c or c == a:
        return 0



def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """Return number of small fruit baskets if it's possible to finish the order, otherwise return -1."""
    total_weight = small_baskets + big_baskets * 5
    if total_weight < ordered_amount:
        return -1
    else:
        required_small_baskets = ordered_amount - big_baskets * 5
        if required_small_baskets <= small_baskets:
            return required_small_baskets
        else:
            return -1
