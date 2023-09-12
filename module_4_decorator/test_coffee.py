import unittest

from coffee import Espresso, Latte
from addons import Milk, Sugar, WhippedCream


class TestDecoratorPattern(unittest.TestCase):
    def test_espresso_cost(self):
        """Test the cost of an Espresso without add-ons."""
        espresso = Espresso()
        self.assertEqual(espresso.get_cost(), 1.5)

    def test_latte_cost(self):
        """Test the cost of a Latte without add-ons."""
        latte = Latte()
        self.assertEqual(latte.get_cost(), 2.0)

    def test_espresso_with_addons_cost(self):
        """Test the cost of an Espresso with multiple add-ons."""
        espresso = Espresso()
        espresso_with_addons = Sugar(Milk(WhippedCream(espresso)))

        self.assertAlmostEqual(espresso_with_addons.get_cost(), 1.5 + 0.2 + 0.3 + 0.5)

    def test_latte_with_addons_cost(self):
        """Test the cost of a Latte with multiple add-ons."""
        latte = Latte()
        latte_with_addons = WhippedCream(Sugar(Milk(latte)))

        self.assertAlmostEqual(latte_with_addons.get_cost(), 2.0 + 0.5 + 0.2 + 0.3)

    def test_dynamic_functionality(self):
        """Test the dynamic functionality of decorators."""
        coffee = Espresso()

        coffee = Milk(coffee)  # Add milk
        self.assertEqual(coffee.get_cost(), 1.5 + 0.3)
        self.assertEqual(coffee.get_description(), "Espresso, Milk")

        coffee = Sugar(coffee)  # Add sugar
        self.assertEqual(coffee.get_cost(), 1.5 + 0.3 + 0.2)
        self.assertEqual(coffee.get_description(), "Espresso, Milk, Sugar")

    def test_flexibility_and_reusability(self):
        """Test the flexibility of using decorators to compose different combinations of coffee and add-ons."""
        coffees = [
            {'coffee': Espresso(), 'addons': [Milk], 'expected_cost': 1.5 + 0.3,
             'expected_description': 'Espresso, Milk'},
            {'coffee': Espresso(), 'addons': [Milk, Sugar], 'expected_cost': 1.5 + 0.3 + 0.2,
             'expected_description': 'Espresso, Milk, Sugar'},
            {'coffee': Latte(), 'addons': [WhippedCream, Milk], 'expected_cost': 2.0 + 0.5 + 0.3,
             'expected_description': 'Latte, Whipped Cream, Milk'}
        ]

        for coffee_data in coffees:
            coffee = coffee_data['coffee']
            addons = coffee_data['addons']
            expected_cost = coffee_data['expected_cost']
            expected_description = coffee_data['expected_description']

            for addon in addons:
                coffee = addon(coffee)

            self.assertAlmostEqual(coffee.get_cost(), expected_cost)
            self.assertEqual(coffee.get_description(), expected_description)

    def test_super_sweet_espresso(self):
        """Test the cost of a super sweet coffee."""
        coffee = Espresso()
        sweet_coffee = Sugar(Sugar(Sugar(Sugar(Sugar(Sugar(Sugar(Sugar(Sugar(Sugar(coffee))))))))))
        self.assertAlmostEqual(sweet_coffee.get_cost(), 1.5 + 0.2 * 10)
        self.assertEqual(sweet_coffee.get_description(), "Espresso, Sugar, Sugar, Sugar, Sugar, Sugar, Sugar, Sugar, Sugar, Sugar, Sugar")

    def test_super_sweet_latte(self):
        """Test the cost of a super sweet coffee."""
        number_of_sugars = 50
        coffee = Latte()
        for _ in range(number_of_sugars):
            coffee = Sugar(coffee)

        self.assertAlmostEqual(coffee.get_cost(), 2.0 + 0.2 * number_of_sugars)
        self.assertEqual(coffee.get_description(), "Latte, " + ", ".join(["Sugar"] * number_of_sugars))
        print(f"Cost of Latte with {number_of_sugars} sugars: {coffee.get_cost()}")
        print(f"Description of Latte with {number_of_sugars} sugars: {coffee.get_description()}")


if __name__ == "__main__":
    unittest.main()
