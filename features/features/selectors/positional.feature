Feature: Positional searching also functions with selectors.

@1
Scenario: I can find elements above a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an InputText above the row containing text "Surname"
  Then I find the element with id: 'nameInput'

@2
Scenario: I can find elements below a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an InputText below the row containing text "Surname"
  Then I find the element with id: 'emailInput'

@3
Scenario: I can find elements left of a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an Input left of the text "Surname"
  Then I find the element with id: 'surnameCheckbox'

@4
Scenario: I can find elements right of a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an Input right of the text "Surname"
  Then I find the element with id: 'surnameInput'

@5
Scenario: I can find td elements right of a specific element.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for an table cell right of the text "Surname"
  Then I find the element with id: 'td22'

@6
Scenario: I can find elements right of an element, but also with indexes.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for all the input texts right of the text "Surname"
  Then I find 6 elements that match
  When I search for the first input text right of the text "Surname"
  Then I find the element with id: 'surnameInput'
  When I search for the second input text right of the text "Surname"
  Then I find the element with id: 'surnameInput2'
  When I search for the third input text right of the text "Surname"
  Then I find the element with id: 'emailInput'
  When I search for the fourth input text right of the text "Surname"
  Then I find the element with id: 'nameInput'
  When I search for the fifth input text right of the text "Surname"
  Then I find the element with id: 'emailInput2'
  When I search for the sixth input text right of the text "Surname"
  Then I find the element with id: 'nameInput2'

@7
Scenario: I can find elements above an element, but also with indexes.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for all the input texts above the text "E-Mail"
  Then I find 4 elements that match
  When I search for the first input text above the text "E-Mail"
  Then I find the element with id: 'surnameInput'
  When I search for the second input text above the text "E-Mail"
  Then I find the element with id: 'surnameInput2'
  When I search for the third input text above the text "E-Mail"
  Then I find the element with id: 'nameInput'
  When I search for the fourth input text above the text "E-Mail"
  Then I find the element with id: 'nameInput2'

@8
Scenario: Filtering elements works even if hidden elements are also matched.
  This is a regression test for offsetParent that can be null in certain scenarios.
  Given I open the browser
  And I go to 'http://localhost:8000/features/test-site/selectors/positional.html'
  When I search for all the elements left of all the elements
  Then there are no elements found

