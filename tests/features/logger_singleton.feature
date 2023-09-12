Feature: Logger Singleton
  As a developer
  I want the Logger class to be a Singleton
  So that I can ensure a single instance and centralize logging

  Background:
    Given the Logger instance is reset

  Scenario: Logger instance creation and comparison
    Given I have requested the Logger instance twice
    Then both instances should be the same object

  Scenario: Write a log message
    Given the Logger instance
    When I log a message "This is a test log message."
    Then the log file should contain the message "This is a test log message."

  Scenario: Raise error when directly instantiating Logger class after getting instance
    Given the Logger instance
    Then directly instantiating Logger should raise a RuntimeError

  Scenario: Raise error when directly instantiating Logger class twice
    Given direct instantiation of the Logger class
    Then directly instantiating Logger again should raise a RuntimeError