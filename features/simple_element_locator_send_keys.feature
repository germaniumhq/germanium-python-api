Feature: Simple Element Locator found elements should function with send_keys
  It seems that when an element was found by the simple locator, sending
  key to it doesn't functions as expected.

  Scenario:
    Given I open firefox
    When I go to 'http://localhost:8000/features/simple/inputs.html'
    Then I type 'input test' into input
    Then the value for the input is 'input test'

