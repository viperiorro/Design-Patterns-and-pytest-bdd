import unittest
from logger import Logger

class TestLoggerSingleton(unittest.TestCase):

    def setUp(self):
        Logger._instance = None  # Reset the singleton instance

    def test_single_instance_directly(self):
        """Test if the same instance is returned on every call."""
        logger1 = Logger()
        self.assertIsNotNone(logger1)  # The object is created

    def test_single_instance(self):
        """Test if the same instance is returned on every call."""
        logger1 = Logger.instance()  # First call
        logger2 = Logger.instance()  # Second call
        self.assertIs(logger1, logger2)  # Both variables refer to the same object

    def test_write_log_message(self):
        """Test if the log message is written to the log file."""
        log_message = "This is a test log message."
        logger = Logger.instance()
        logger.log(log_message)  # Write a log message to the log file

        # Read the log file and check if the message is there
        with open("log.txt", "r") as log_file:
            content = log_file.read()
            self.assertIn(log_message, content)

    def test_raise_error_when_instance_exists(self):
        """Test if an error is raised when trying to instantiate the Logger class directly."""
        logger = Logger.instance()
        with self.assertRaises(RuntimeError):
            Logger()

    def test_raise_error_when_called_twice(self):
        """Test if an error is raised when trying to instantiate the Logger class directly."""
        logger = Logger()
        with self.assertRaises(RuntimeError):
            Logger()
