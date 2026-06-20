from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [
        pytest.param(5, 8, 26, id="perimeter_integer"),
        pytest.param(2.6, 5.5, 16.2, id="perimeter_float")
    ]
)
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f"Perimeter of the rectangle with sides {r.side_a, r.side_b} must be {perimeter}, actual is {r.perimeter}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        pytest.param(3, 5, 15, id="area_integer"),
        pytest.param(2.8, 3.2, 2.8 * 3.2, id="area_float")
    ]
)
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Area of the rectangle with sides {r.side_a, r.side_b} must be {area}, actual is {r.area}"


@pytest.mark.negative
@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        pytest.param(-5, 5, id="negative_side_a_integer"),
        pytest.param(-5.2, 5.2, id="negative_side_a_float"),
        pytest.param(2, -3, id="negative_side_b_integer"),
        pytest.param(3.2, -2.2, id="negative_side_b_float"),
        pytest.param(0, 2, id="zero_side_a_integer"),
        pytest.param(0.0, 8, id="zero_side_a_float"),
        pytest.param(5, 0, id="zero_side_b_integer"),
        pytest.param(2.2, 0.0, id="zero_side_b_float"),
        pytest.param(0, 0, id="zero_both_integer"),
        pytest.param(0.0, 0.0, id="zero_both_float"),
    ]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError, match=f"Sides must be above zero, current side_a = {side_a} and side_b = {side_b}"):
        Rectangle(side_a, side_b)
