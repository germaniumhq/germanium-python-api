Feature: Positional access to elements.

  @1
  Scenario Outline: clicking on the top left of an item works as expected (<Div Id>, <Point Location>)
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/position/position.html'
    When I click on the <Point Location> corner of '<Div Id>'
    Then the text of the '#messagesDiv' is '<Expected Message>'
    Examples:
      | Div Id       | Point Location | Expected Message   |
      | #inlineDiv   | top left       | inline x: 0 y: 0   |
      | #absoluteDiv | top left       | absolute x: 0 y: 0 |

  @2
  Scenario Outline: clicking on the top right of an item works as expected (<Div Id>, <Point Location>)
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/position/position.html'
    When I click on the <Point Location> corner of '<Div Id>'
    Then the text of the '#messagesDiv' is '<Expected Message>'
    Examples:
      | Div Id       | Point Location | Expected Message     |
      | #inlineDiv   | top right      | inline x: 299 y: 0   |
      | #absoluteDiv | top right      | absolute x: 299 y: 0 |


  @3
  Scenario Outline: clicking on the bottom left of an item works as expected (<Div Id>, <Point Location>)
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/position/position.html'
    When I click on the <Point Location> corner of '<Div Id>'
    Then the text of the '#messagesDiv' is '<Expected Message>'
    Examples:
      | Div Id       | Point Location | Expected Message     |
      | #inlineDiv   | bottom left    | inline x: 0 y: 199   |
      | #absoluteDiv | bottom left    | absolute x: 0 y: 199 |

  @4
  Scenario Outline: clicking on the bottom right of an item works as expected (<Div Id>, <Point Location>)
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/position/position.html'
    When I click on the <Point Location> corner of '<Div Id>'
    Then the text of the '#messagesDiv' is '<Expected Message>'
    Examples:
      | Div Id       | Point Location | Expected Message       |
      | #inlineDiv   | bottom right   | inline x: 299 y: 199   |
      | #absoluteDiv | bottom right   | absolute x: 299 y: 199 |

