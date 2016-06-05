Feature: Test the `@iframe` decorator.
    Switching, and in general iframe management is pretty painful.
    Germanium allows specifying an iframe strategy, that will be
    used to centralize all the iframe management into only one place.

Scenario: Test if the iframe changes the context to the specified iframe.
    Given I open the browser
    And I go to 'http://localhost:8000/features/test-site/iframe-inputs.html'
    When I type into iframe in input#textInput the following text: input test
    Then in the iframe the value for the input#textInput is 'input test'
