import unittest


from module_3_abstract_factory.gui.factory import WindowsGUIFactory, MacGUIFactory

class TestButton(unittest.TestCase):

    windows_factory = WindowsGUIFactory()  # Create instances of the Windows factory
    mac_factory = MacGUIFactory()  # Create instances of the Mac factory
    factories = [windows_factory, mac_factory]  # Create a list of all factories

    def test_windows_and_mac_factories_create_buttons_of_same_parent_type(self):
        """Test that the Windows and Mac factories create buttons that are instances of the same parent class."""
        # Create instances of the Windows and Mac buttons
        windows_button = self.windows_factory.create_button()
        mac_button = self.mac_factory.create_button()

        # Get the parent class of the Windows and Mac buttons
        windows_button_parent = windows_button.__class__.__bases__[0]
        mac_button_parent = mac_button.__class__.__bases__[0]

        # Assert that the parent classes of the Windows and Mac buttons are the same
        self.assertEqual(windows_button_parent, mac_button_parent)

    def test_factories_create_buttons_of_same_parent_type(self):
        """Test that the factories create buttons that are instances of the same parent class."""
        # Create instances of all buttons
        buttons = [factory.create_button() for factory in self.factories]

        # Get the parent class of all buttons
        button_parents = [button.__class__.__bases__[0] for button in buttons]

        # Get all unique parent classes (if there is only one, all buttons are instances of the same parent class)
        unique_button_parents = set(button_parents)

        # Assert that there is only one unique parent class
        self.assertEqual(len(unique_button_parents), 1)

