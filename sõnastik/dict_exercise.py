def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    return hobbies_dict.get(name, "name not in dictionary")


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest person in given dictionary.

    :param height_dict: dictionary with peoples' names and heights
    :return: name of tallest person in given dict.
    """
    tallest = max(height_dict, key=height_dict.get)
    return tallest


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are divisible by six are removed.

    :param six_dict: dictionary to be modified.
    :return: dict without values that are divisible by six.
    """
    return {key: value for key, value in six_dict.items() if value % 6 != 0}


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    return {v: k for k, v in exchange_dict.items()}


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    symbol_count = {}
    for char in stringy:
        symbol_count[char] = symbol_count.get(char, 0) + 1
    return symbol_count


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key is the first symbol and the value is a list of words starting with this symbol.

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    organised_dict = {}
    for string in strings:
        first_char = string[0]
        organised_dict.setdefault(first_char, []).append(string)
    return organised_dict
