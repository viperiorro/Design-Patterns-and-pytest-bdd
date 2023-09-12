import unittest


from module_3_abstract_factory.gui.factory import WindowsGUIFactory, MacGUIFactory


class TestCheckbox(unittest.TestCase):

    windows_factory = WindowsGUIFactory()  # Create instances of the Windows factory
    mac_factory = MacGUIFactory()  # Create instances of the Mac factory
    factories = [windows_factory, mac_factory]  # Create a list of all factories

    def test_windows_and_mac_factories_create_checkboxes_of_same_parent_type(self):
        """Test that the Windows and Mac factories create checkbox that are instances of the same parent class."""
        # Create instances of the Windows and Mac checkbox
        windows_checkbox = self.windows_factory.create_checkbox()
        mac_checkbox = self.mac_factory.create_checkbox()

        # Get the parent class of the Windows and Mac checkbox
        windows_checkbox_parent = windows_checkbox.__class__.__bases__[0]
        mac_checkbox_parent = mac_checkbox.__class__.__bases__[0]

        # Assert that the parent classes of the Windows and Mac checkbox are the same
        self.assertEqual(windows_checkbox_parent, mac_checkbox_parent)

    def test_factories_create_checkboxes_of_same_parent_type(self):
        """Test that the factories create checkbox that are instances of the same parent class."""
        # Create instances of all checkbox
        checkbox = [factory.create_checkbox() for factory in self.factories]

        # Get the parent class of all checkbox
        checkbox_parents = [checkbox.__class__.__bases__[0] for checkbox in checkbox]

        # Get all unique parent classes (if there is only one, all checkbox are instances of the same parent class)
        unique_checkbox_parents = set(checkbox_parents)

        # Assert that there is only one unique parent class
        self.assertEqual(len(unique_checkbox_parents), 1)