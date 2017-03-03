Feature: Test the Box API.

  @1
  Scenario: Elements that are not found should be reported nicely
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/position/position.html'
    When I try to get the box positions for a selector that doesn't matches
    Then I get an exception spelling out that my selector didn't matched
    # And not a random JS error :)
