Feature: Opening a firefox browser works out of the box.

  Scenario: Open Google
    Given I open firefox
    When I go to 'http://google.com'
    Then the title of the page contains 'Google'
