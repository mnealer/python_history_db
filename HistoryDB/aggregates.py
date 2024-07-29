from abc import ABC, abstractmethod


class Aggregate(ABC):

    @abstractmethod
    def inner_function(self):
        pass

    @abstractmethod
    def outer_function(self):
        pass


