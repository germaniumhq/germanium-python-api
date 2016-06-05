Feature: get_text utility function.
  Using get_text a user can get the text of an element as a
  simple String, irrespective if the element is visible or not.

@1
Scenario: Check reading text from a visible div
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/get-text.html'
  And I get the text from element '#visibleTextDiv'
  Then the text from that element is
  """
  Some visible text
  Yay
  """

@2
Scenario: Check reading text from an invisible div
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/get-text.html'
  And I get the text from element '#displayNoneTextDiv'
  Then the text from that element is
  """
  Some invisible text
  """

@3
Scenario: Check reading text from a visible span
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/get-text.html'
  And I get the text from element '#containingVisibleText'
  Then the text from that element is
  """
  visible text
  """

@4
Scenario: Check reading text from an invisible span
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/get-text.html'
  And I get the text from element '#containingInvisibleText'
  Then the text from that element is
  """
  invisible text
  """

@5
Scenario: Check reading text from a pre element
  Given I open the browser
  When I go to 'http://localhost:8000/features/test-site/get-text.html'
  And I get the text from element '#preElement'
  Then the text from that element is
  """
  Some
  text   in   a   pre
  element
  """
