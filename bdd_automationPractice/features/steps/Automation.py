import behave
from selenium import webdriver
from nose.tools import assert_true,assert_equal

@given("the user is in main page")
def step_impl(context):

    context.browser = webdriver.Firefox(executable_path = r"/home/esteban/programacion/python3/3.automation/driverFirefox")
    context.browser.implicitly_wait(5)
    context.browser.get("http://automationpractice.com/index.php")

@when("the user push the button ContactUs")
def step_impl(context):

    context.browser.find_element_by_link_text("Contact us").click()

@then("the user is in contact page")
def step_impl(context):

    assert_true("CUSTOMER SERVICE - CONTACT US" in context.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/h1").text)
#
@when("the user push the button SignIn")
def step_impl(context):
    
    context.browser.find_element_by_link_text("Sign in").click()

@then("the user is in Sign page")
def step_impl(context):

    assert_true("AUTHENTICATION" in context.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/h1").text)
#
@when("the user search '{item}'")
def step_impl(context, item):

    context.browser.find_element_by_id("search_query_top").send_keys(item)
    context.browser.find_element_by_name("submit_search").click()

@then("the user should see '{item}' title")
def step_impl(context, item):

    assert_true(item.upper() in context.browser.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/h1/span[1]").text)









