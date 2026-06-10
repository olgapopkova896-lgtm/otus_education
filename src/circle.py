from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: int | float):
        if r <= 0:
            raise ValueError(f'Radius must be above zero, current r = {r}')
        self.r = r

    @property
    def perimeter(self) -> int | float:
        return 2 * pi * self.r

    @property
    def area(self) -> int | float:
        return pi * self.r ** 2
