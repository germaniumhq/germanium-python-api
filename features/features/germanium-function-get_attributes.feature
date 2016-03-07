Feature: get_attributes utility function.
  Using get_attributes a user can get all the attributes
  of an element into a single map.

  Scenario:
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/get-attributes.html'
    And I get the #myElement element attributes
    Then there are 4 attributes
    And the attribute 'id' is 'myElement'
    And the attribute 'class' is 'meta what bad / sad'
    And the attribute 'style' is 'border: black'
    And the attribute 'custom-attribute' is 'random value'
