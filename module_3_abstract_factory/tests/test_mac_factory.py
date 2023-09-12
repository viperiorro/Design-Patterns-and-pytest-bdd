import unittest

from module_3_abstract_factory.gui.elements.button import Button, MacButton
from module_3_abstract_factory.gui.elements.checkbox import Checkbox, MacCheckbox
from module_3_abstract_factory.gui.factory import MacGUIFactory


class TestMacFactory(unittest.TestCase):

    def test_mac_factory_creates_mac_button(self):
        mac_factory = MacGUIFactory()
        button = mac_factory.create_button()
        self.assertIsInstance(button, MacButton)

    def test_mac_factory_creates_mac_checkbox(self):
        mac_factory = MacGUIFactory()
        checkbox = mac_factory.create_checkbox()
        self.assertIsInstance(checkbox, MacCheckbox)

    def test_mac_factory_creates_button_instance(self):
        mac_factory = MacGUIFactory()
        button = mac_factory.create_button()
        self.assertIsInstance(button, Button)

    def test_mac_factory_creates_checkbox_instance(self):
        mac_factory = MacGUIFactory()
        checkbox = mac_factory.create_checkbox()
        self.assertIsInstance(checkbox, Checkbox)