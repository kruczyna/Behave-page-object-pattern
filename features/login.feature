Feature: Login

  Scenario Outline: I want to navigate to Sign In form
    Given I navigate to Sign In form
    When I submit "<email>" and "<password>"
    Then I see form "<error>" massage
    Examples:
      | email                           | password | error                  |
      | wdwd                            | wdwd     | invalid email address  |
      | authentication_failed@email.com | Test     | authentication failed  |
      |                                 | cscsc    | email address required |
