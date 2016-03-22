Feature: inside/containing feature check for selectors.

@1
Scenario: I can find elements inside a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for an InputText inside the div with id inputTextContainer
  Then I find the element with id: 'inputText'

@2
Scenario: Finding elements that are inside CSS elements raises exceptions.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div inside a CSS selector
  Then it throws an exception

@3
Scenario: I can find elements that contain specific elements.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div containing an InputText
  Then I find the element with id: 'inputTextContainer'

@4
Scenario: Finding elements that contain CSS elements raises exceptions.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div containing a CSS selector
  Then it throws an exception
