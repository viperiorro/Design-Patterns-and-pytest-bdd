Feature: GUI elements factories
  As a developer
  I want to use the proper factory for creating GUI elements
  So that the appropriate elements are created for each GUI type

  Scenario Outline: Factories create buttons and checkboxes of the correct type
    Given factory "<factory_type>"
    When it creates a button
    And it creates a checkbox
    Then the button should be of the type "<button_type>"
    Then the checkbox should be of the type "<checkbox_type>"

    Examples:
      | factory_type      | button_type   | checkbox_type   |
      | WindowsGUIFactory | WindowsButton | WindowsCheckbox |
      | MacGUIFactory     | MacButton     | MacCheckbox     |

  Scenario: Factories create buttons and checkboxes of the same parent type
    Given all factories
    When they create buttons
    And they create checkboxes
    Then all buttons should have the same parent type
    And all checkboxes should have the same parent type

  Scenario: Adding a new factory and GUI elements
    Given a new GUI factory
    When it creates a button
    And it creates a checkbox
    Then the button should be of the type "NewButton"
    Then the checkbox should be of the type "NewCheckbox"