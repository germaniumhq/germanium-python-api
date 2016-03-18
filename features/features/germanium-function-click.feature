Feature: Using germanium should be easy to right click, click or double click.
    When having a WebDriver object it's pretty tricky to do
    basic operations such as right click or click. For example
    clicking on an element can easily be done via `element
    .click()`, but for doing a right click it becomes necessary
    to create an ActionChain, and then pass the element into the
    ActionChain.

@1
Scenario: Basic click
      Given I open firefox
      And I go to 'http://localhost:8000/features/test-site/mouse.html'
      When I click on .eventTargetDiv
      Then the value for the input#textInput is 'click'

@2
Scenario: Right click
      Given I open firefox
      And I go to 'http://localhost:8000/features/test-site/mouse.html'
      When I right click on .eventTargetDiv
      Then the value for the input#textInput is 'contextmenu'

@3
Scenario: Double click
      Given I open firefox
      And I go to 'http://localhost:8000/features/test-site/mouse.html'
      When I doubleclick on .eventTargetDiv
      Then the value for the input#textInput is 'doubleclick'

@4
Scenario: Hover over
      Given I open firefox
      And I go to 'http://localhost:8000/features/test-site/mouse.html'
      When I mouse over on .eventTargetDiv
      Then the value for the input#textInput is 'mouseover'

