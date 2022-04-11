Feature: Sign in
  Scenario: User try sign in using valid data from header menu
    Given User is on the Home Page
    When User chooses Sign In button
    And User fills in email address and password on sign in area
    And User chooses Sign in padlock button
    Then User is Sign in


  Scenario: User try sign in using invalid password
    Given User is on the Home Page
    When User chooses Sign In button
    And User fills in email address and invalid password on sign in area
    And User chooses Sign in padlock button
    Then User gets message about failed authentication