Feature: text selector.

Scenario: Find an element that contains some text.
    Given I open firefox
    And I go to 'http://localhost:8000/features/simple/selectors/text.html'
    When I look for some text: 'just a simple div'
    Then I find the element with id: 'simpleText'

Scenario: Find an element that contains some text with multiple matches.
    Given I open firefox
    And I go to 'http://localhost:8000/features/simple/selectors/text.html'
    When I look for some text: 'multimatch'
    Then I find the element with id: 'multimatchspan'

Scenario: Find an element that contains some text that is formatted:
    Given I open firefox
    And I go to 'http://localhost:8000/features/simple/selectors/text.html'
    When I look for some text: 'some formatted text'
    Then I find the element with id: 'formattedText'

