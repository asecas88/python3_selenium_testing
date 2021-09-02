from behave import *
from selenium import webdriver
from nose.tools import assert_true

@given("The user is in main page")
def step_impl(context):

    context.browser = webdriver.Firefox(executable_path = r"/home/esteban/programacion/python3/3.automation/driverFirefox")
    context.browser.get("https://www.mercadolibre.com.ar/")
    context.browser.implicitly_wait(5)

@when("The user search '{item}'")
def step_impl(context, item):

    context.browser.find_element_by_name("as_word").send_keys(item)
    context.browser.find_element_by_xpath("/html/body/header/div/form/button/div").click()

@then("The user is in '{item}' page")
def step_impl(context, item):

    assert_true(item.capitalize() in context.browser.find_element_by_xpath("/html/body/main/div/div[1]/aside/div[1]/h1").text)
