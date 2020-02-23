Feature: Login

  Scenario Outline: As a user I can't login with invalid credentials
    Given I navigate to Sign In form
    When I submit "<email>" and "<password>"
    Then I see form "<error>" massage
    Examples:
      | email                           | password     | error                  |
      | wdwd                            | wdwd         | invalid email address  |
      | authentication_failed@email.com | Test         | invalid password       |
      | authentication_failed@email.com | Testtttttttt | authentication failed  |
      |                                 | cscsc        | email address required |

  Scenario: As a user I can login to the website
    Given I navigate to Sign In form
    When I submit "v.k@mail.com" and "test1234"
    Then I am a logged in user
