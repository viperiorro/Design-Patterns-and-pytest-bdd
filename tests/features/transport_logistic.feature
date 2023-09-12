Feature: Transport and Logistic factories
  As a developer
  I want to use the proper factory for each transport type
  So that the appropriate delivery method is used

  @automated
  Scenario Outline: Factory creates appropriate transport types
    Given logistic "<logistic_type>"
    When using the logistic
    Then it should create transport "<transport_type>"

    Examples:
      | logistic_type | transport_type |
      | RoadLogistic  | Truck          |
      | SeaLogistic   | Ship           |
      | AirLogistic   | Airplane       |

  @automated
  Scenario Outline: Plan delivery using different transport types
    Given logistic "<logistic_type>"
    When plan delivery to "<destination>"
    Then the output should be "Delivering by <transport_type> to the destination: <destination>"

    Examples:
      | logistic_type | transport_type | destination |
      | RoadLogistic  | Truck          | New York    |
      | SeaLogistic   | Ship           | London      |
      | AirLogistic   | Airplane       | Paris       |

  @automated
  Scenario: All factories create only transports
    Given all logistics
    When using the logistics
    Then they should create only transports

  @planned
  Scenario: New factory can be added
    Given new factory
    When using the factory
    Then it should create transport
