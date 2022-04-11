Feature: Sign up
  Scenario: User try create account using valid data
    Given User is on the Home Page
    When User chooses Sign In button
    And User fills in email address on create account area
    And User chooses Create and account button
    And User fills all necessary information in sign up form
    And User chooces Register button
    Then User is sign in

  Scenario: User try create account using already registered e-mail
    Given User is on the Home Page
    When User chooses Sign In button
    And User fills in already used email address on create account area
    Then User get information about already registered email
