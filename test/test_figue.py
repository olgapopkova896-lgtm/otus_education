from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
import pytest
from math import pi


@pytest.mark.parametrize(
    ("figure_a", "figure_b", "sum_area"),
    [
        pytest.param(Circle(1), Circle(1), 2 * pi, id="two_circles"),
        pytest.param(Rectangle(2, 3), Rectangle(2, 3), 12.0, id="two_rectangles"),
        pytest.param(Square(2), Square(2), 8.0, id="two_squares"),
        pytest.param(Triangle(3, 4, 5), Triangle(3, 4, 5), 12.0, id="two_triangles"),
        pytest.param(Circle(1), Rectangle(2, 3), pi + 6, id="circle_and_rectangle"),
        pytest.param(Circle(1), Square(2), pi + 4, id="circle_and_square"),
        pytest.param(Circle(1), Triangle(3, 4, 5), pi + 6, id="circle_and_triangle"),
        pytest.param(Rectangle(2, 3), Circle(1), 6 + pi, id="rectangle_and_cycle"),
        pytest.param(Rectangle(2, 3), Square(2), 10, id="rectangle_and_square"),
        pytest.param(Rectangle(2, 3), Triangle(3, 4, 5), 12, id="rectangle_and_triangle"),
        pytest.param(Square(2), Circle(1), pi + 4, id="square_and_circle"),
        pytest.param(Square(2), Rectangle(2, 3), 10, id="square_and_rectangle"),
        pytest.param(Square(2), Triangle(3, 4, 5), 10, id="square_and_triangle"),
        pytest.param(Triangle(3, 4, 5), Circle(1), 6 + pi, id="triangle_and_cycle"),
        pytest.param(Triangle(3, 4, 5), Square(2), 10, id="triangle_and_square"),
        pytest.param(Triangle(3, 4, 5), Rectangle(2, 3), 12, id="triangle_and_rectangle"),
    ]
)
def test_figure_add_area(figure_a, figure_b, sum_area, start_session):
    assert figure_a.add_area(
        figure_b) == sum_area, f"Sum of areas are not as expected {sum_area}, actual is {figure_a.add_area(figure_b)}"


@pytest.mark.negative
@pytest.mark.parametrize(
    "figure_b",
    [
        pytest.param(5, id="negative_integer"),
        pytest.param(3.5, id="negative_float"),
        pytest.param("test", id="negative_string"),
    ]
)
def test_figure_add_area_negative(figure_b):
    figure_a = Circle(1)
    with pytest.raises(ValueError, match="Argument figure must be Figure"):
        figure_a.add_area(figure_b)
