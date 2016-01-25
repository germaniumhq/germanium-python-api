Feature: The S super locator, that returns deferred locators.

Scenario: Find by inferred CSS locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/simple/inputs.html'
    Then I type 'input test' into input
    Then the value for the input is 'input test'

Scenario: Find by inferred XPath locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/simple/inputs.html'
    Then I type 'input test' into //input
    Then the value for the //input is 'input test'

Scenario: Find by inferred simple locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/simple/inputs.html'
    Then I type 'input test' into "Text input" > input
    Then the value for the "Text input" > input is 'input test'

Scenario: Finding elements that don't exist should not throw exceptions
    Given I open firefox
    When I go to 'http://localhost:8000/features/simple/inputs.html'
    And I search for //does/not/exist
    And I search for div.what
    And I search for div["what"].what
    Then nothing happens
