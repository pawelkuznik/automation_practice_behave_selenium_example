Feature: Add to cart feature
  Scenario Outline:The user is able to add an item to the cart after it has been found by the search engine
    Given User is on the Home Page
    When User enters the <item_name>
    And User chooses item from drop-down list
    And User changes color
    And User click Add to cart button
    Then Item is added to the cart

    Examples:
    | item_name |
    | Faded Short Sleeve T-shirts |


   Scenario Outline: The user is able to add an item to the cart from products grid view
     Given User is on the Home Page
     When User chooses Women category
     And User chooses <subcategory> subcategory
     And User add to cart first item from list
     Then Item is added to the cart

     Examples:
     | subcategory |
     |T-shirts    |
     |Blouses     |