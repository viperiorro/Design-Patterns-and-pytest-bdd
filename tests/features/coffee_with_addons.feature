Feature: Coffee orders with add-ons
  As a customer
  I want to order coffee with add-ons
  So that my coffee order is customized to my preference

  Scenario Outline: Order coffee with add-ons
    Given I have a "<coffee_type>" coffee
    When I add the following add-ons <add_ons>
    Then the final cost should be <final_cost>
    And the final description should be "<final_description>"

    Examples:
      | coffee_type | add_ons             | final_cost | final_description             |
      | Espresso    | Milk                | 1.8        | Espresso, Milk                |
      | Espresso    | Sugar, Milk         | 2.0        | Espresso, Sugar, Milk         |
      | Latte       | WhippedCream, Milk  | 2.8        | Latte, Whipped Cream, Milk    |
      | Espresso    | Sugar, Sugar, Sugar | 2.1        | Espresso, Sugar, Sugar, Sugar |

  Scenario: Test the cost of a super sweet Latte
    Given I have a "Latte" coffee
    When I add 50 "Sugar" add-ons
    Then the final cost should be 12.0
    And the final description should be "Latte, Sugar, Sugar, Sugar, Sugar, ..., Sugar" with 50 Sugars
