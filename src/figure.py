from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure) -> int | float:
        if not isinstance(figure, Figure):
            raise ValueError(f'Argument figure must be Figure or child class, current {type(figure)}')
        return self.area + figure.area
