import pytest
from main import fit_transform


def test_default():
    with pytest.raises(TypeError):
        fit_transform(1)


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "Moscow",
                "New York",
                "Moscow",
                "London",
            ],
            [
                ("Moscow", [0, 0, 1]),
                ("New York", [0, 1, 0]),
                ("Moscow", [0, 0, 1]),
                ("London", [1, 0, 0]),
            ],
        ),
        (
            [
                "green",
                "yellow",
                "black",
                "purple",
            ],
            [
                ("green", [0, 0, 0, 1]),
                ("yellow", [0, 0, 1, 0]),
                ("black", [0, 1, 0, 0]),
                ("purple", [1, 0, 0, 0]),
            ],
        ),
    ],
)
def test_inputs(input, expected):
    assert fit_transform(input) == expected


def test_string():
    assert fit_transform("hi") == [("hi", [1])]
