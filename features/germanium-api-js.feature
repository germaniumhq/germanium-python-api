Feature: The js API.

Scenario: Call a JS Script with a custom argument.
    Given I open firefox
    And I go to 'http://localhost:8000/features/simple/inputs.html'
    When I execute js with one parameter 'jsparameter'
    """
    if (arguments.length == 0) {
        throw new Error("Expected one argument");
    }

    if (arguments[0] != "jsparameter") {
        throw new Error("The parameter is " + arguments[0] + " instead of `jsparameter`");
    }
    """
    Then nothing happens

