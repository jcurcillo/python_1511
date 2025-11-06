import pytest
from Lab11_jcurcillo import simplify_rotation, negative_simplify_rotation, type_verification

def test_normal_input():
    assert simplify_rotation(100) == 100
    assert simplify_rotation(460) == 100
    assert simplify_rotation(820) == 100

def test_negative_input():
    assert negative_simplify_rotation(-100) == 100
    assert negative_simplify_rotation(-460) == 100
    assert negative_simplify_rotation(-820) == 100

def test_string_input():
    with pytest.raises(ValueError):
        type_verification('Hello')