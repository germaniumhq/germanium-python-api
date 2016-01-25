Feature: Germanium enabled typing of the keys.
    In regular APIs sending keys quickly becomes a chore, since we need to
    always create all kinds of composite actions in order to send something
    such as <ctrl-B>.

    Germanium abstracts this API into a sane single string format, allowing
    also typings such as: <!shift><right><right><^shift>, that means pressing
    shift down, and keeping it pressed, then twice the right key, then releasing
    the shift key.

    Scenario:
      Given I open firefox
      When I go to 'http://localhost:8000/features/simple/inputs.html'
      And I click on input#textInput
      And I type_keys 'input test<tab>'
      Then the value for the input#textInput is 'input test'
      And I type_keys 'another input teST<bs><bs>st'
      Then the value for the input#anotherTextInput is 'another input test'
      And I type_keys '<!shift><left><left><left><^shift><bs>EST'
      Then the value for the input#anotherTextInput is 'another input tEST'
      And I type_keys '<ctrl-shift-left><bs>test'
      Then the value for the input#anotherTextInput is 'another input test'

