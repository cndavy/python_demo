# -*- coding: utf-8 -*-
from time import sleep


__author__ = 'han'
from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager


def input_frame(browser, attribute):
    xpath = "//input[@id='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False


def click_button(browser, attribute):
    xpath = "//input[@id='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False

def searchword(browser,attribute):
    xpath = "//a[em]"
    elems = browser.find_elements_by_xpath(xpath)
    for elem in elems:
        if attribute in elem.text:
            return True

    return   False

# 定位输入框输入关键字
@step('I fill in field with id "(.*?)" with "(.*?)"')
def baidu_text(step, field_name, value):
    with AssertContextManager(step):
        text_field = input_frame(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value)


#点击“百度一下”按钮
@step('I click id "(.*?)" with baidu once')
def baidu_click(step, field_name):
    with AssertContextManager(step):
        click_field = click_button(world.browser, field_name)
        click_field.click()




@step('I should see "(.*?)" within (\d+) second')
def  baidu_check(step,text1,time):
     with AssertContextManager(step):
         waiting=int(time)
         sleep(waiting)
         word=searchword(world.browser,text1)

#关闭浏览器

@step('I close browser')
def close_browser(step):
    world.browser.quit()