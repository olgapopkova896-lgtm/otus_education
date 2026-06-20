from src.circle import Circle
from math import pi
import pytest


@pytest.mark.parametrize(
    ("r", "perimeter"),
    [
        pytest.param(5, 2 * pi * 5, id="perimeter_integer_r"),
        pytest.param(2.5, 2 * pi * 2.5, id="perimeter_float_r")
    ]
)
def test_circle_perimeter(r, perimeter, start_file):
    c = Circle(r)
    assert c.perimeter == perimeter, f"Perimeter of the circle with radius {c.r} must be {perimeter}, actual is {c.perimeter}"


@pytest.mark.parametrize(
    ("r", "area"),
    [
        pytest.param(5, pi * 5 ** 2, id="area_integer_r"),
        pytest.param(2.5, pi * 2.5 ** 2, id="area_float_r")
    ]
)
def test_circle_area(r, area, start_test):
    c = Circle(r)
    assert c.area == area, f"Area of the circle with radius {c.r} must be {area}, actual is {c.area}"


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
