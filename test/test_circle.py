from src.circle import Circle
from math import pi, pow
import pytest


def test_circle_perimeter(circle):
    assert circle.perimeter == 2 * pi * circle.r, f"Perimeter of the circle with radius {circle.r} must be {2 * pi * circle.r}, actual is {circle.perimeter}"


def test_circle_area(circle):
    assert circle.area == pi * pow(circle.r,
                                   2), f"Area of the circle with radius {circle.r} must be {pi * pow(circle.r, 2)}, actual is {circle.area}"


@pytest.mark.negative
@pytest.mark.parametrize(
    "r",
    [
        -5, -2.5, 0, 0.0,
    ],
    ids=["negative_integer_r", "negative_float_r", "zero_integer", "zero_float"]
)
def test_circle_negative_value(r):
    with pytest.raises(ValueError, match="Radius must be above zero"):
        Circle(r)
