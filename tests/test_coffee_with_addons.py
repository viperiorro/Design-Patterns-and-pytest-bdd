import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from module_4_decorator.addons import Milk, Sugar, WhippedCream
from module_4_decorator.coffee import Espresso, Latte

scenarios("coffee_with_addons.feature")

coffee_classes = {"Espresso": Espresso, "Latte": Latte}
addon_classes = {"Milk": Milk, "Sugar": Sugar, "WhippedCream": WhippedCream}


@given(parsers.parse("I have a \"{coffee_type}\" coffee"), target_fixture="coffee")
def order_coffee(coffee_type):
    return coffee_classes[coffee_type]()


@when(parsers.parse("I add the following add-ons {add_ons}"), target_fixture="coffee_with_addons")
def add_addons(coffee, add_ons):
    addons = [addon_classes[addon.strip()] for addon in add_ons.split(",")]

    for addon in addons:
        coffee = addon(coffee)

    return coffee


@when("I add 50 \"Sugar\" add-ons", target_fixture="coffee_with_addons")
def add_50_sugars(coffee):
    for _ in range(50):
        coffee = Sugar(coffee)

    return coffee


@then(parsers.parse("the final cost should be {final_cost}"))
def check_final_cost(coffee_with_addons, final_cost):
    assert coffee_with_addons.get_cost() == pytest.approx(float(final_cost))


@then(parsers.parse("the final description should be \"{final_description}\""))
def check_final_description(coffee_with_addons, final_description):
    assert coffee_with_addons.get_description() == final_description


@then("the final description should be \"Latte, Sugar, Sugar, Sugar, Sugar, ..., Sugar\" with 50 Sugars")
def check_final_description_for_50_sugars(coffee_with_addons):
    assert coffee_with_addons.get_description() == "Latte, " + ", ".join(["Sugar"] * 50)
