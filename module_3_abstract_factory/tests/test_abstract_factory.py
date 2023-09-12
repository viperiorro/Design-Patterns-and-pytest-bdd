import unittest

from module_3_abstract_factory.gui.elements.button import Button
from module_3_abstract_factory.gui.elements.checkbox import Checkbox
from module_3_abstract_factory.gui.factory import GUIFactory, WindowsGUIFactory, MacGUIFactory

class TestAbstractFactoryPattern(unittest.TestCase):

    def test_extensibility(self):
        """
        This test highlights how the Abstract Factory pattern is easily extensible.
        Adding a new GUI with its respective elements does not require changing the existing code.
        """
        class NewGUIFactory(GUIFactory):
            def create_button(self):
                return NewButton()

            def create_checkbox(self):
                return NewCheckbox()

        class NewButton(Button):
            def click(self):
                return "New Button clicked"

        class NewCheckbox(Checkbox):
            def check(self):
                return "New Checkbox checked"

        new_factory = NewGUIFactory()
        button = new_factory.create_button()
        checkbox = new_factory.create_checkbox()

        self.assertIsInstance(button, Button)
        self.assertIsInstance(checkbox, Checkbox)
        self.assertEqual(button.click(), "New Button clicked")
        self.assertEqual(checkbox.check(), "New Checkbox checked")

    def test_switch_between_guis(self):
        """
        This test demonstrates the flexibility of the Abstract Factory pattern.
        By modifying only the factory used, we can switch between different GUIs
        without major changes in the overall code structure.
        """
        guis = [
            {'factory': WindowsGUIFactory(), 'name': 'Windows'},
            {'factory': MacGUIFactory(), 'name': 'Mac'}
        ]

        for gui in guis:
            factory = gui['factory']
            name = gui['name']

            button = factory.create_button()
            checkbox = factory.create_checkbox()

            self.assertIsInstance(button, Button)
            self.assertIsInstance(checkbox, Checkbox)
            self.assertEqual(button.click(), f"{name} Button clicked")
            self.assertEqual(checkbox.check(), f"{name} Checkbox checked")

    def test_switching_between_guis_with_new_gui(self):
        """
        This test demonstrates the flexibility of the Abstract Factory pattern.
        By modifying only the factory used, we can switch between different GUIs
        without major changes in the overall code structure.
        """
        class NewGUIFactory(GUIFactory):
            def create_button(self):
                return NewButton()

            def create_checkbox(self):
                return NewCheckbox()

        class NewButton(Button):
            def click(self):
                return "New Button clicked"

        class NewCheckbox(Checkbox):
            def check(self):
                return "New Checkbox checked"

        guis = [
            {'factory': WindowsGUIFactory(), 'name': 'Windows'},
            {'factory': MacGUIFactory(), 'name': 'Mac'},
            {'factory': NewGUIFactory(), 'name': 'New'}
        ]

        for gui in guis:
            factory = gui['factory']
            name = gui['name']

            button = factory.create_button()
            checkbox = factory.create_checkbox()

            self.assertIsInstance(button, Button)
            self.assertIsInstance(checkbox, Checkbox)
            self.assertEqual(button.click(), f"{name} Button clicked")
            self.assertEqual(checkbox.check(), f"{name} Checkbox checked")


if __name__ == "__main__":
    unittest.main()