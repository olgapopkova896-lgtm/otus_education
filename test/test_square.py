from src.square import Square
import pytest


@pytest.mark.parametrize(
    ("side_a", "perimeter"),
    [
        pytest.param(5, 20, id="perimeter_integer"),
        pytest.param(2.6, 10.4, id="perimeter_float")
    ]
)
def test_square_perimeter(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f"Perimeter of the square with sides {s.side_a} must be {perimeter}, actual is {s.perimeter}"


@pytest.mark.parametrize(
    ("side_a", "area"),
    [
        pytest.param(3, 9, id="area_integer"),
        pytest.param(2.8, 2.8 * 2.8, id="area_float")
    ]
)
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Area of the square with sides {s.side_a} must be {area}, actual is {s.area}"


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
