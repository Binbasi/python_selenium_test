Feature: run a browser test with selenium and behave

  Scenario: user has opened browser with blank tab
    When Go to https://www.a1.digital
    When accept all cookies
    When go to "Lösungen" page
    Then go to "Exoscale" page



