from abc import ABC, abstractmethod


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox checked"


class MacCheckbox(Checkbox):
    def check(self):
        return "Mac Checkbox checked"