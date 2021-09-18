import behave                                                    # must install behave library
from selenium import webdriver                                   # must install selenium library  
from nose.tools import assert_true,assert_equal                  # must install nose library

from pages.pageIndex import PageIndex
from pages.pageContact import PageContact
from pages.pageSign import PageSign
from pages.pageItem import PageItem


@given("the user is in main page")
def step_impl(context):
                         # Firefox webdriver                       configurate webdriver dir 
    context.browser = webdriver.Firefox(executable_path = r"/your webdriver dir.../driverFirefox")
    context.browser.implicitly_wait(5)
    context.browser.get("http://automationpractice.com/index.php")

@when("the user push the button ContactUs")
def step_impl(context):

    pageIndex = PageIndex(context.browser)
    pageIndex.contact_button_click()               

@then("the user is in contact page")
def step_impl(context):

    pageContact = PageContact(context.browser)

    assert_true("CUSTOMER SERVICE - CONTACT US" in pageContact.title_text())    
#
@when("the user push the button SignIn")                                              
def step_impl(context):

    pageIndex = PageIndex(context.browser)

    pageIndex.sign_in_button_click()

@then("the user is in Sign page")                                        
def step_impl(context):

    pageSign = PageSign(context.browser)

    assert_true("AUTHENTICATION" in pageSign.title_text())
#
@when("the user search '{item}'")                                             
def step_impl(context, item):

    pageIndex = PageIndex(context.browser)

    pageIndex.searchbox_search_word(item)

@then("the user should see '{item}' title")
def step_impl(context, item):

    pageItem = PageItem(context.browser)
    
    assert_true(item.upper() in pageItem.title_text())








