from abc import ABC, abstractmethod


class Aggregate(ABC):

    def __init__(self, field):
        self.field = field

    @abstractmethod
    def inner_function(self):
        pass

    @abstractmethod
    def outer_function(self):
        pass


