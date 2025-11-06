import pytest
from example_code import divide, is_even


def test_divide_with_correct_input():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == None

def test_divide_using_strings():
    assert divide(10, '2') == None

#next

def test_is_even_correct_inputs():
    assert is_even(5) == False
    assert is_even(10) == True

def test_is_even_float_number_input():
    assert is_even(6.6) == False

def test_is_even_string_input():
    assert is_even('hello') == None


   