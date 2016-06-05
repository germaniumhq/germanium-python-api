Feature: get_attributes utility function.
  Using get_attributes a user can get all the attributes
  of an element into a single map.

  Scenario:
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/parent_node.html'
    When I get the parent node of the element with id 'childDiv'
    Then I find the element with id: 'expectedParent'
