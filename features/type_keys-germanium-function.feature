Feature: Germanium enabled typing of the keys.
    In regular APIs sending keys quickly becomes a chore, since we need to
    always create all kinds of composite actions in order to send something
    such as <ctrl-B>.

    Scenario:
      Given I open firefox
      When I go to 'http://localhost:8000/simple/inputs.html'
      And I click on input#textInput
      And I type_keys 'input test<tab>another input teST<bs><bs>st'
      Then the value for the input#textInput is 'input test'
      And the value for the input#anotherTextInput is 'another input test'
