Feature: The S super locator, that returns deferred locators.

@1
Scenario: Find by inferred CSS locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into input
    Then the value for the input is 'input test'

@2
Scenario: Find by inferred XPath locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into //input
    Then the value for the //input is 'input test'

@3
Scenario: Find by inferred simple locators.
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then I type 'input test' into simple:"Text input" > input
    Then the value for the simple:"Text input" > input is 'input test'

@4
Scenario: Finding elements that don't exist should not throw exceptions
    Given I open firefox
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    And I search using S for //does/not/exist
    And I search using S for div.what
    And I search using S for div["what"].what
    Then nothing happens
