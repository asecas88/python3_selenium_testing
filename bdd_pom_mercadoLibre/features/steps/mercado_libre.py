from behave import *                             # must install behave library
from selenium import webdriver                   # must install selenium library   
from nose.tools import assert_true               # must install nose library
from pages.pageIndex import *
from pages.pageItem import *
from pages.pageRegistration import *
from pages.pageLogin import *


@given("The user is in main page")
def step_impl(context):
                    # Firefox webdriver                         configurate webdriver dir                                                
    context.browser = webdriver.Firefox(executable_path = r"/your webdriver dir.../driverFirefox")
    context.browser.get("https://www.mercadolibre.com.ar/")
    context.browser.implicitly_wait(5)

@when("The user search '{item}'")
def step_impl(context, item):

    pageIndex = PageIndex(context.browser)

    pageIndex.search_box_find_item(item)

@then("The user is in '{item}' page")
def step_impl(context, item):

    pageItem = PageItem(context.browser)

    assert_true(item.capitalize() in pageItem.title_text())

#-------------------------

@when("The user clicks Crea Tu Cuenta button")
def step_impl(context):

    pageIndex = PageIndex(context.browser)

    pageIndex.crea_tu_cuenta_button_click()

@then("The user is in registration page")
def step_impl(context):

    pageRegistration = PageRegistration(context.browser)

    assert_true("Completá tus datos" in pageRegistration.title_text())

#--------------------------

@when("The user clicks Ingresa button")
def step_impl(context):

    pageIndex = PageIndex(context.browser)

    pageIndex.ingresa_button_click()

@then("The user is in login page")
def step_impl(context):

    pageLogin = PageLogin(context.browser)

    assert_true('teléfono' and 'e-mail' and 'usuario' in pageLogin.title_text())
    
#--------------------------

@when("The user clicks in Mis Compras button")
def step_impl(context):

    pageIndex = PageIndex(context.browser)

    pageIndex.mis_compras_button_click()








                                                          

