Feature: Opening a firefox browser works out of the box.

  Scenario: Open a simple page
    Given I open the browser
    When I go to 'http://localhost:8000/features/test-site/inputs.html'
    Then the title of the page equals 'INPUTS Page'
