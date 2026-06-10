from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int | float):
        if side_a <= 0:
            raise ValueError(f'Sides must be above zero, current side_a = {side_a}')
        super().__init__(side_a, side_a)
