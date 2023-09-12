from abc import abstractmethod, ABC


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        return "Windows Button clicked"


class MacButton(Button):
    def click(self):
        return "Mac Button clicked"