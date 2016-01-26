Feature: Germanium enabled typing of the keys.
    In regular APIs sending keys quickly becomes a chore, since we need to
    always create all kinds of composite actions in order to send something
    such as <ctrl-B>.

    Germanium abstracts this API into a sane single string format, allowing
    also typings such as: <!shift><right><right><^shift>, that means pressing
    shift down, and keeping it pressed, then twice the right key, then releasing
    the shift key.

    @scenario1
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

    @scenario2
    Scenario: Ensure all the keycodes are passed correctly
      Given I open firefox
      And I go to 'http://localhost:8000/features/simple/key_type-support.html'
      And I click on body
      Then I type_keys '<ctrl-a><del>'
      And I type_keys 'qw<CR>as<CR>'
      And I type_keys '<up><home><right><!shift><right><right><^shift>'
      And I type_keys '<ctrl-b><ctrl-end>'
      And I type_keys '<ctrl-z>'
      And I type_keys '<ctrl-z>'
      Then there is no error message.
