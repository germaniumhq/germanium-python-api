Feature: Positional access to elements.

@1
Scenario: clicking on the top left of an item works as expected on inline elements
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/position/position.html'
  When I click on the top left corner of '#inlineDiv'
  Then the text of the '#messagesDiv' is 'inline x: 0 y: 0'

@2
Scenario: clicking on the top left of an item works as expected on absolute elements
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/position/position.html'
  When I click on the top left corner of '#absoluteDiv'
  Then the text of the '#messagesDiv' is 'absolute x: 0 y: 0'

@3
Scenario: clicking on the top right of an item works as expected on inline elements
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/position/position.html'
  When I click on the top right corner of '#inlineDiv'
  Then the text of the '#messagesDiv' is 'inline x: 399 y: 0'

@4
Scenario: clicking on the top right of an item works as expected on absolute elements
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/position/position.html'
  When I click on the top right corner of '#absoluteDiv'
  Then the text of the '#messagesDiv' is 'absolute x: 399 y: 0'
