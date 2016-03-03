Feature: XPath Selector

@1
Scenario: Find an input button using JsSelector.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/button.html'
  When I look for the following js selector: return document.getElementById('inputButton')
  Then I find the element with id: 'inputButton'
