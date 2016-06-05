Feature: Selectors should provide some means of getting the
  elements out. For example, when someone wants to get if
  the element exists, it usually wants to check with:
  assert Text('whatever').exists()
  instead of:
  assert S(Text('whatever')).exists()

@1
Scenario: I can find a single element using directly the selector
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search using selectors for an InputText above the text "Surname"
  Then I find the element with id: 'nameInput'

@2
Scenario: I can find an element list using directly the selector
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search using selectors for all InputText elements
  Then I find 6 text elements that match

@3
Scenario: I can find if a element exists using directly the selector
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search using selectors if an InputText above the text "Surname" exists
  Then yes, it exists

@4
Scenario: I can find if a element exists using directly the selector
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search using selectors if an Image above the text "Surname" exists
  Then no, it doesn't exists

@5
Scenario: I can find an element from the element list using its index.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search using a Css selector for the 3rd 'input'
  Then I find the element with id: 'surnameCheckbox'
