Feature: Positional searching also functions with selectors.

@1
Scenario: I can find elements above a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for a TextInput above the text "Surname"
  Then I find the element with id: 'nameInput'

@2
Scenario: I can find elements below a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for a TextInput below the text "Surname"
  Then I find the element with id: 'emailInput'

@3
Scenario: I can find elements left of a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an Input left of the text "Surname"
  Then I find the element with id: 'surnameCheckbox'

@4
Scenario: I can find elements right of a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for a Input right of the text "Surname"
  Then I find the element with id: 'surnameInput'
