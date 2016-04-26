Feature: Positional searching also functions with selectors.

@1
Scenario: I can find elements above a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an InputText above the row containing text "Surname"
  Then I find the element with id: 'nameInput'

@2
Scenario: I can find elements below a specific element.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an InputText below the row containing text "Surname"
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
  When I search for an Input right of the text "Surname"
  Then I find the element with id: 'surnameInput'

@5
Scenario: I can find elements right of an element, but also with indexes.
  Given I open firefox
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for the first input text of the text "Surname"
  Then I find the element with id: 'surnameInput'
  When I search for the second input text of the text "Surname"
  Then I find the element with id: 'surnameInput2'
  When I search for the third input text of the text "Surname"
  Then I find the element with id: 'emailInput'
  When I search for the fourth input text of the text "Surname"
  Then I find the element with id: 'emailInput2'
  When I search for the fifth input text of the text "Surname"
  Then I find the element with id: 'nameInput'
  When I search for the sixth input text of the text "Surname"
  Then I find the element with id: 'nameInput2'
