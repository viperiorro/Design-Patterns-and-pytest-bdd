from abc import ABC

from module_4_decorator.coffee import Coffee


# Define the abstract Decorator class, which also implements the Coffee interface
class CoffeeAddon(Coffee, ABC):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()


# Implement concrete decorator classes for add-ons (Milk, WhippedCream, Sugar)
class Milk(CoffeeAddon):
    def get_cost(self):
        return self._coffee.get_cost() + 0.3

    def get_description(self):
        return self._coffee.get_description() + ", Milk"


class WhippedCream(CoffeeAddon):
    def get_cost(self):
        return self._coffee.get_cost() + 0.5

    def get_description(self):
        return self._coffee.get_description() + ", Whipped Cream"


class Sugar(CoffeeAddon):
    def get_cost(self):
        return self._coffee.get_cost() + 0.2

    def get_description(self):
        return self._coffee.get_description() + ", Sugar"
