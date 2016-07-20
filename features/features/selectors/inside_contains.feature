Feature: inside/containing feature check for selectors.

@1
Scenario: I can find elements inside a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for an InputText inside the div with id inputTextContainer
  Then I find the element with id: 'inputText'

@2
Scenario: I can find elements inside a specific element using CSS.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search using CSS for an input inside the div#inputTextContainer
  Then I find the element with id: 'inputText'

@3
Scenario: Finding elements inside non CSS/XPath locators is raising exceptions.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div inside a JS selector
  Then I find the element with id: 'inputTextContainer'

@4
Scenario: I can find elements that contain specific elements.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div containing an InputText
  Then I find the element with id: 'inputTextContainer'

@5
Scenario: I can find elements that contain specific elements using CSS.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search using CSS for a div containing an InputText
  Then I find the element with id: 'inputTextContainer'

@6
Scenario: Finding elements containing CSS/XPath locators is raising exceptions.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for a div containing a JS selector
  Then I find the element with id: 'inputTextContainer'

@7
Scenario: Finding elements without children should find only those that actually have no children
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for all the divs without children
  Then I only get the div with id #decoyDiv

@8
Scenario: Finding elements without children might also return no elements, even if there are elements with children
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for all the spans without children
  Then I get no elements returned

@9
Scenario: Finding elements using indexes should construct the correct XPath
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/inside_contains.html'
  When I search for the first input in the second div
  Then I find the element with id: 'inputText'