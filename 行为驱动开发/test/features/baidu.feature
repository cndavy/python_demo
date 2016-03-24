Feature: Go to baidu  

Scenario: search lettuce_webdriver
  Given I go to "http://www.baidu.com/"  
     When I fill in field with id "kw" with "韩同超"
     And  I click id "su" with baidu once
     Then I should see "韩同超" within 2 second
     Then I close browser