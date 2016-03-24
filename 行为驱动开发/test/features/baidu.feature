Feature: Go to baidu  
  
Scenario: search selenium  
  Given I go to "http://www.baidu.com/"  
     When I fill in field with id "kw" with "selenium"
     And  I click id "su" with baidu once
     Then I should see "seleniumhq.org" within 2 second

Scenario: search lettuce_webdriver
  Given I go to "http://www.baidu.com/"  
     When I fill in field with id "kw" with "lettuce_webdriver"
     And  I click id "su" with baidu once
     Then I should see "pypi.python.org" within 2 second
     Then I close browser