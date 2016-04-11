Feature: Simple alert support should function.

Scenario: Open a simple page
  Given I open firefox
  When I go to 'http://localhost:8000/features/test-site/alert/alert_alert.html'
  Then there is an alert that exists
  And the text of the alert is "alert is present"
  And I close the alert dialog by ok

