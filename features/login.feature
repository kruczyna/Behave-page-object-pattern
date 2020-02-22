Feature: Login

  Scenario Outline: I want to navigate to Sign In form
    Given I navigate to Sign In form
    When I submit "<email>" and "<password>"
    Examples:
      | email | password |
      | wdwd  | wdwd     |
