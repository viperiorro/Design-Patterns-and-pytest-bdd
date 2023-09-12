import unittest

from module_3_abstract_factory.gui.elements.button import Button, WindowsButton
from module_3_abstract_factory.gui.elements.checkbox import Checkbox, WindowsCheckbox
from module_3_abstract_factory.gui.factory import WindowsGUIFactory


class TestWindowsFactory(unittest.TestCase):

    def test_windows_factory_creates_windows_button(self):
        windows_factory = WindowsGUIFactory()
        button = windows_factory.create_button()
        self.assertIsInstance(button, WindowsButton)

    def test_windows_factory_creates_windows_checkbox(self):
        windows_factory = WindowsGUIFactory()
        checkbox = windows_factory.create_checkbox()
        self.assertIsInstance(checkbox, WindowsCheckbox)

    def test_windows_factory_creates_button_instance(self):
        windows_factory = WindowsGUIFactory()
        button = windows_factory.create_button()
        self.assertIsInstance(button, Button)

    def test_windows_factory_creates_checkbox_instance(self):
        windows_factory = WindowsGUIFactory()
        checkbox = windows_factory.create_checkbox()
        self.assertIsInstance(checkbox, Checkbox)

if __name__ == "__main__":
    unittest.main()