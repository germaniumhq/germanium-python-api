Feature: Button selector.

Scenario: Find an input button.
    Given I open firefox
    And I go to 'http://localhost:8000/features/test-site/selectors/button.html'
    When I look for a button with the text: 'Input Button'
    Then I find the element with id: 'inputButton'

Scenario: Find an input button by name.
    Given I open firefox
    And I go to 'http://localhost:8000/features/test-site/selectors/button.html'
    When I look for a button with the name: 'inputButton'
    Then I find the element with id: 'inputButton'

Scenario: Find a real button.
    Given I open firefox
    And I go to 'http://localhost:8000/features/test-site/selectors/button.html'
    When I look for a button with the text: 'Real Button'
    Then I find the element with id: 'realButton'

Scenario: Find a real button by name.
    Given I open firefox
    And I go to 'http://localhost:8000/features/test-site/selectors/button.html'
    When I look for a button with the name: 'realButton'
    Then I find the element with id: 'realButton'


