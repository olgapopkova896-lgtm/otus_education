from src.square import Square
import pytest


def test_square_perimeter(square):
    assert square.perimeter == 4 * square.side_a, f"Perimeter of the square with sides {square.side_a} must be {4 * square.side_a}, actual is {square.perimeter}"


def test_square_area(square):
    assert square.area == square.side_a * square.side_a, f"Area of the square with sides {square.side_a} must be {square.side_a * square.side_a}, actual is {square.area}"


@pytest.mark.negative
@pytest.mark.parametrize(
    ("side_a"),
    [
        pytest.param(-5, id="negative_integer"),
        pytest.param(-5.2, id="negative_float"),
        pytest.param(0, id="zero_integer"),
        pytest.param(0.0, id="zero_float"),
    ]
)
def test_square_negative(side_a):
    with pytest.raises(ValueError, match=f"Sides must be above zero, current side_a = {side_a}"):
        Square(side_a)
