import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from module_1_singleton.logger import Logger

# Load the feature file
scenarios('logger_singleton.feature')  # All scenarios will be loaded from the specified file


@given("the Logger instance is reset")
def reset_logger_instance():
    """Reset the singleton instance before each test."""
    Logger._instance = None


@given("the Logger instance", target_fixture="logger_instance")
def logger_instance():
    return Logger.instance()


# Step definitions
@given("I have requested the Logger instance twice", target_fixture="request_logger_instance_twice")
def request_logger_instance_twice():
    logger1 = Logger.instance()
    logger2 = Logger.instance()
    return logger1, logger2


@then("both instances should be the same object")
def check_instances(request_logger_instance_twice):
    assert request_logger_instance_twice[0] is request_logger_instance_twice[1]


@when(parsers.parse('I log a message "{message}"'))
def log_message(logger_instance, message):
    logger_instance.log(message)


@then(parsers.parse('the log file should contain the message "{expected_message}"'))
def check_log_file(expected_message):
    with open("log.txt", "r") as log_file:
        content = log_file.read()
        assert expected_message in content


@then("directly instantiating Logger should raise a RuntimeError")
def attempt_direct_instantiation_after_getting_instance(logger_instance):
    with pytest.raises(RuntimeError):
        Logger()


@given("direct instantiation of the Logger class", target_fixture="direct_instance")
def direct_instance():
    return Logger()


@then("directly instantiating Logger again should raise a RuntimeError")
def attempt_direct_instantiation_twice(direct_instance):
    with pytest.raises(RuntimeError):
        Logger()
