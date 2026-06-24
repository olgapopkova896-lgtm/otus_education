from src.triangle import Triangle
import pytest
from math import sqrt


def test_triangle_perimeter(triangle):
    expected_perimeter = triangle.side_a + triangle.side_b + triangle.side_c
    assert triangle.perimeter == expected_perimeter, f"Perimeter of the triangle with sides {triangle.side_a, triangle.side_b, triangle.side_c} must be {expected_perimeter}, actual is {triangle.perimeter}"


def test_triangle_area(triangle):
    pp = (triangle.side_a + triangle.side_b + triangle.side_c) / 2
    expected_area = sqrt(pp * (pp - triangle.side_a) * (pp - triangle.side_b) * (pp - triangle.side_c))
    assert triangle.area == expected_area, f"Area of the triangle with sides {triangle.side_a, triangle.side_b, triangle.side_c} must be {expected_area}, actual is {triangle.area}"


@pytest.mark.negative
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        pytest.param(-5, 5, 8, id="negative_side_a_integer"),
        pytest.param(-5.2, 5.2, 7.8, id="negative_side_a_float"),
        pytest.param(2, -3, 4, id="negative_side_b_integer"),
        pytest.param(3.2, -2.2, 3.4, id="negative_side_b_float"),
        pytest.param(2, 3, -4, id="negative_side_c_integer"),
        pytest.param(3.2, 3.2, -3.4, id="negative_side_c_float"),
        pytest.param(0, 2, 3, id="zero_side_a_integer"),
        pytest.param(0.0, 8, 5, id="zero_side_a_float"),
        pytest.param(5, 0, 3, id="zero_side_b_integer"),
        pytest.param(2.2, 0.0, 3, id="zero_side_b_float"),
        pytest.param(5, 4, 0, id="zero_side_c_integer"),
        pytest.param(2.2, 3.4, 0.0, id="zero_side_c_float"),
        pytest.param(0, 0, 0, id="zero_all_integer"),
        pytest.param(0.0, 0.0, 0.0, id="zero_all_float"),
    ]
)
def test_square_negative_less_zero(side_a, side_b, side_c):
    with pytest.raises(ValueError,
                       match=f"Sides must be above zero, current side_a = {side_a}, side_b = {side_b}, side_c = {side_c}"):
        Triangle(side_a, side_b, side_c)


@pytest.mark.negative
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        pytest.param(2, 3, 5, id="negative_side_a_and_side_b_equals_side_c_integer"),
        pytest.param(5.2, 4.2, 9.4, id="negative_side_a_and_side_b_equals_side_c_float"),
        pytest.param(6, 2, 4, id="negative_side_b_and_side_c_equals_side_a_integer"),
        pytest.param(6.6, 2.2, 3.4, id="negative_side_b_and_side_c_equals_side_a_float"),
        pytest.param(2, 7, 5, id="negative_side_a_and_side_c_equals_side_b_integer"),
        pytest.param(2.2, 6.6, 3.4, id="negative_side_a_and_side_c_equals_side_b_float"),
        pytest.param(2, 5, 3, id="negative_side_a_and_side_b_less_side_c_integer"),
        pytest.param(5.2, 4.1, 9.4, id="negative_side_a_and_side_b_less_side_c_float"),
        pytest.param(6, 2, 3, id="negative_side_b_and_side_c_less_side_a_integer"),
        pytest.param(6.6, 2.1, 3.4, id="negative_side_b_and_side_c_less_side_a_float"),
        pytest.param(2, 8, 5, id="negative_side_a_and_side_c_less_side_b_integer"),
        pytest.param(5.2, 15.6, 9.4, id="negative_side_a_and_side_c_less_side_b_float"),
    ]
)
def test_square_negative_non_existent(side_a, side_b, side_c):
    with pytest.raises(ValueError,
                       match=f"This triangle does not exist side_a = {side_a}, side_b = {side_b}, side_c = {side_c}"):
        Triangle(side_a, side_b, side_c)
