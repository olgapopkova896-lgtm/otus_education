from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
import pytest


@pytest.fixture(params=[5, 2.5], ids=["integer_r", "float_r"])
def circle(request):
    return Circle(request.param)


@pytest.fixture(params=[(5, 8), (2.6, 5.5)], ids=["integer_sides", "float_sides"])
def rectangle(request):
    side_a, side_b = request.param
    return Rectangle(side_a, side_b)


@pytest.fixture(params=[5, 2.6], ids=["integer_sides", "float_sides"])
def square(request):
    return Square(request.param)


@pytest.fixture(params=[(5, 6, 7), (2.6, 3.33, 4.67)], ids=["integer_sides", "float_sides"])
def triangle(request):
    side_a, side_b, side_c = request.param
    return Triangle(side_a, side_b, side_c)
