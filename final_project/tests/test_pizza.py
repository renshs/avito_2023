import pytest
from src.pizza import Margherita, Hawaiian, Pepperoni, Pizza


def test_worng_sieze_type():
    with pytest.raises(TypeError):
        Pizza(1)


def test_wrong_size_value():
    with pytest.raises(ValueError):
        Pizza("M")


def test_equal():
    p_1 = Margherita()
    p_2 = Margherita()
    assert p_1 == p_2


def test_not_equal():
    p_1 = Margherita()
    p_2 = Pepperoni()
    assert p_1 != p_2
