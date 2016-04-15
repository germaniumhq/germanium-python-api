Feature: Implement selection of elements in <select> HTML objects.
  In regular APIs selecting an element from a Select it's buried deep
  inside webdriver code. It would be nice to have an API that allows
  selecting items with ease, just like a regular action.

@1
Scenario: On a page with a select, I can select its value by its text
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/select.html'
  When I select in the first select the entry with text 'A1'
  Then the value in the first select is 'a1value'

@2
Scenario: On a page with a select, I can select its value by its value
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/select.html'
  When I select in the first select the entry with value 'a2value'
  Then the value in the first select is 'a2value'

@3
Scenario: On a page with a select, I can select its value by its index
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/select.html'
  When I select in the first select the entry with index 3
  Then the value in the first select is 'a3value'


