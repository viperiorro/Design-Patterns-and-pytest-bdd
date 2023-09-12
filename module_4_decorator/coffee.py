from abc import ABC, abstractmethod


# Define the Component (Coffee) interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


# Implement the concrete Coffee types (Espresso, Latte)
class Espresso(Coffee):
    def get_cost(self):
        return 1.5

    def get_description(self):
        return "Espresso"


class Latte(Coffee):
    def get_cost(self):
        return 2.0

    def get_description(self):
        return "Latte"
