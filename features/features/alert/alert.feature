Feature: Simple alert support should function.

@1
Scenario: Test a basic alert
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_alert.html'
  Then there is an alert that exists
  And the text of the alert is "alert is present"
  And I close the alert dialog by ok

@2
Scenario: Test a Confirmation by clicking the OK button
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_confirm.html'
  Then there is an alert that exists
  And the text of the alert is "confirm dialog"
  And I close the alert dialog by ok
  Then the text of the page is
  """
  CONFIRM ACCEPTED
  """

@3
Scenario: Test a Confirmation by clicking the CANCEL button
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_confirm.html'
  Then there is an alert that exists
  And the text of the alert is "confirm dialog"
  And I close the alert dialog by cancel
  Then the text of the page is
  """
  CONFIRM REJECTED
  """

@4
Scenario: Test an Prompt by rejecting it.
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_prompt.html'
  Then there is an alert that exists
  And the text of the alert is "prompt alert"
  And I close the alert dialog by cancel
  Then the text of the page is
  """
  PROMPT REJECTED
  """

@5
Scenario: Test an Prompt by setting some value using regular type_keys with an Alert.
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_prompt.html'
  Then there is an alert that exists
  And the text of the alert is "prompt alert"
  When I write into the alert 'prompt input'
  And I close the alert dialog by ok
  Then the text of the page is
  """
  prompt input
  """

@6
Scenario: Test an Prompt by setting some value using type_keys on the alert instance.
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_prompt.html'
  Then there is an alert that exists
  And the text of the alert is "prompt alert"
  When I write into the alert using Alert().send_keys 'prompt input'
  And I close the alert dialog by ok
  Then the text of the page is
  """
  prompt input
  """

@7
Scenario: Test an Prompt by setting some value using type_keys, with an 'alert' Super selector.
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_prompt.html'
  Then there is an alert that exists
  And the text of the alert is "prompt alert"
  When I write into the alert using type_keys(.., 'alert') 'prompt input'
  And I close the alert dialog by ok
  Then the text of the page is
  """
  prompt input
  """

@8
Scenario: Test an Prompt by setting some value using type_keys without a selector, by means of 'alert' detection.
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/alert/alert_prompt.html'
  Then there is an alert that exists
  And the text of the alert is "prompt alert"
  When I type_keys 'prompt input'
  And I close the alert dialog by ok
  Then the text of the page is
  """
  prompt input
  """
