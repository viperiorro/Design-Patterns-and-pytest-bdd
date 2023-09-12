from abc import ABC, abstractmethod

from module_3_abstract_factory.gui.elements.button import WindowsButton, MacButton
from module_3_abstract_factory.gui.elements.checkbox import WindowsCheckbox, MacCheckbox


# Define the module_3_abstract_factory interface for creating GUI elements
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Create the concrete factory for the Windows GUI library
class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# Create the concrete factory for the Mac GUI library
class MacGUIFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
