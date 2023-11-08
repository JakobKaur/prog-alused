import math
from math import sqrt
def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum_result = num_a + num_b
    difference_result = num_a - num_b
    return sum_result, difference_result

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division_result = num_a / num_b
    return division_result

def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division_result = num_a // num_b
    return division_result

def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = pow(num_a, num_b)
    remainder = num_a % num_b
    return multiply_numbers, power, remainder

def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average

def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * (radius ** 2) 
    return circle_area

def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = (sqrt(3) / 4) * (side_length ** 2)
    return triangle_area

def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = (b ** 2) - (4 * a * c)
    return discriminant

def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = sqrt(a**2 + b**2)
    return c

def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = sqrt(c**2 - a**2)
    return b