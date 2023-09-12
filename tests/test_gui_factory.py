from pytest_bdd import given, when, then, parsers, scenarios

from module_3_abstract_factory.gui.elements.button import Button, WindowsButton, MacButton
from module_3_abstract_factory.gui.elements.checkbox import Checkbox, WindowsCheckbox, MacCheckbox
from module_3_abstract_factory.gui.factory import GUIFactory, WindowsGUIFactory, MacGUIFactory

scenarios("gui_factory.feature")

factory_classes = {
    "WindowsGUIFactory": WindowsGUIFactory,
    "MacGUIFactory": MacGUIFactory,
}
button_classes = {
    "WindowsButton": WindowsButton,
    "MacButton": MacButton,
}
checkbox_classes = {
    "WindowsCheckbox": WindowsCheckbox,
    "MacCheckbox": MacCheckbox,
}


@given(parsers.parse('factory "{factory_type}"'), target_fixture="factory")
def get_factory(factory_type):
    return factory_classes[factory_type]()


@given("a new GUI factory", target_fixture="factory")
def get_new_factory():
    class NewButton(Button):
        def click(self):
            return "New Button clicked"

    class NewCheckbox(Checkbox):
        def check(self):
            return "New Checkbox checked"

    class NewGUIFactory(GUIFactory):
        def create_button(self):
            return NewButton()

        def create_checkbox(self):
            return NewCheckbox()

    button_classes["NewButton"] = NewButton
    checkbox_classes["NewCheckbox"] = NewCheckbox

    return NewGUIFactory()


@when("it creates a button", target_fixture="button")
def create_button(factory):
    return factory.create_button()


@when("it creates a checkbox", target_fixture="checkbox")
def create_checkbox(factory):
    return factory.create_checkbox()


@then(parsers.parse('the button should be of the type "{button_type}"'))
def assert_button_type(button, button_type):
    assert isinstance(button, button_classes[button_type])


@then(parsers.parse('the checkbox should be of the type "{checkbox_type}"'))
def assert_checkbox_type(checkbox, checkbox_type):
    assert isinstance(checkbox, checkbox_classes[checkbox_type])


@given("all factories", target_fixture="all_factories")
def get_all_factories():
    return [f() for f in factory_classes.values()]


@when("they create buttons", target_fixture="buttons")
def create_all_buttons(all_factories):
    return [factory.create_button() for factory in all_factories]


@when("they create checkboxes", target_fixture="checkboxes")
def create_all_checkboxes(all_factories):
    return [factory.create_checkbox() for factory in all_factories]


@then("all buttons should have the same parent type")
def buttons_have_same_parent_type(buttons):
    button_parents = {button.__class__.__bases__[0] for button in buttons}
    assert len(button_parents) == 1


@then("all checkboxes should have the same parent type")
def checkboxes_have_same_parent_type(checkboxes):
    checkbox_parents = {checkbox.__class__.__bases__[0] for checkbox in checkboxes}
    assert len(checkbox_parents) == 1
