from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f'Sides must be above zero, current side_a = {side_a}, side_b = {side_b}, side_c = {side_c}')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError(f'This triangle does not exist side_a = {side_a}, side_b = {side_b}, side_c = {side_c}')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self) -> int | float:
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self) -> float:
        pp = self.perimeter / 2
        return sqrt(pp * (pp - self.side_a) * (pp - self.side_b) * (pp - self.side_c))
