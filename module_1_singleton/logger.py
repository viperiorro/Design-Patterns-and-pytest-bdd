import os


class Logger:
    _instance = None

    @classmethod
    def instance(cls):
        # Return the single instance of the Logger class, or create it if it doesn't exist.
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __new__(cls):
        """
        The __new__ method is responsible for the actual object creation process.
        It's a special method in Python classes involved in the process of instantiating an object.
        The __new__ method is called before __init__ and returns a new object (possibly of a different type).

        In the Logger Singleton class, __new__ checks if an instance already exists;
        if so, it raises an error to prevent multiple instances.
        If no instance exists, it creates the object using the superclass's __new__ method.
        """
        if cls._instance:
            raise RuntimeError("Call `instance()` method instead of instantiating `Logger` class directly.")
        else:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __init__(self):
        """
        The __init__ method is called after the object is created with __new__.
        It's meant for object-specific initialization, such as setting the default values of attributes.

        In the Logger Singleton class, __init__ sets up the log file by removing it if it already exists.
        This ensures a clean log file for each instance of the Logger.
        Since the Logger class is a Singleton, __init__ will only be called once when the first instance is created.
        """
        self._log_file = "log.txt"
        if os.path.exists(self._log_file):
            os.remove(self._log_file)

    def log(self, message):
        # Write a message to the log file.
        with open(self._log_file, "a") as log_file:
            log_file.write(f"{message}\n")