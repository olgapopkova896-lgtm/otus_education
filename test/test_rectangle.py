from src.rectangle import Rectangle
import pytest


def test_rectangle_perimeter(rectangle):
    assert rectangle.perimeter == 2 * (
            rectangle.side_a + rectangle.side_b), f"Perimeter of the rectangle with sides {rectangle.side_a, rectangle.side_b} must be {2 * (
            rectangle.side_a + rectangle.side_b)}, actual is {rectangle.perimeter}"


def test_rectangle_area(rectangle):
    assert rectangle.area == rectangle.side_a * rectangle.side_b, f"Area of the rectangle with sides {rectangle.side_a, rectangle.side_b} must be {rectangle.side_a * rectangle.side_b}, actual is {rectangle.area}"


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
