Feature: Opening a firefox browser works out of the box.

  Scenario: Open a simple page
    Given I open firefox
    When I go to 'http://localhost:8000/simple/inputs.html'
    Then the title of the page equals 'INPUTS Page'
