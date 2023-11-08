"""Math exercises vol2."""

import math

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    # Write your code here
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    # Write your code here
    angle_radians = math.radians(angle)
    sine = round(math.sin(angle_radians), 2)
    cosine = round(math.cos(angle_radians), 2)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    # Write your code here
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    # Write your code here
    string_numbers = str(num_a + num_b)
    return string_numbers