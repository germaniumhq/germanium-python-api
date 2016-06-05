Feature: text selector.

@1
Scenario: Find an element that contains some text.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text: 'just a simple div'
    Then I find the element with id: 'simpleText'

@2
Scenario: Find an element that contains some text with multiple matches.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text: 'multimatch'
    Then I find the element with id: 'multimatchspan'

@3
Scenario: Find an element that contains some text that is formatted:
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text: 'some formatted text'
    Then I find the element with id: 'formattedText'

@4
Scenario: Find an element that contains some text that has double quotes.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text: 'a "text" with quotes'
    Then I find the element with id: 'textWithQuotes'

@5
Scenario: Find an element that contains some text that has single quotes.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text: 'a 'text' with quotes'
    Then I find the element with id: 'textWithSingleQuotes'

@6
Scenario: Finding multiple text elements that match across the document.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/selectors/text.html'
    When I look for some text in multiple elements: 'text'
    Then I find 5 text elements that match
