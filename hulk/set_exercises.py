def create_set_from_numbers(a: int, b: int, c: int) -> set:
    """
    Create set from three integers.
    """
    return {a, b, c}


def add_one(set_a: set) -> set:
    """
    Take a set of integers and increment each integer by one, return new set.
    """
    return {x + 1 for x in set_a}


def remove_six(set_a: set) -> set:
    """
    Take a set of digits and remove the number six from it if it's there, return set.
    """
    return set_a - {6}


def convert_to_set(list_a: list) -> set:
    """
    Take a list, convert it to a set, and return it.
    """
    return set(list_a)


def count_unique_elements(input_list: list) -> int:
    """
    Count unique elements in the list.
    """
    return len(set(input_list))


def common_characters_in_words(word1: str, word2: str) -> set:
    """
    Find common characters in two words.
    """
    return set(word1) & set(word2)


def exam_conditions_not_met(names1: list, names2: list) -> set:
    """
    Who has NOT met the conditions for the exam.
    """
    return set(names1) ^ set(names2)


def uninvited_friends_count(friends: list, invited: list) -> int:
    """
    How many friends were not invited.
    """
    return len(set(friends) - set(invited))


def contains_duplicates(input_list: list) -> bool:
    """
    Return whether the list contains duplicate elements.
    """
    return len(input_list) != len(set(input_list))


def find_numbers_divisible_by_3(numbers: list) -> set:
    """
    Return a set of numbers from the input list which are divisible by 3.
    """
    return set(num for num in numbers if num % 3 == 0)