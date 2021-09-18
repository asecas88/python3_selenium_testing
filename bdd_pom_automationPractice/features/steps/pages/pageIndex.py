from selenium.webdriver.common.by import By


class PageIndex(object):

    def __init__(self, my_driver):

        self.driver = my_driver
        self.contact_button = (By.LINK_TEXT, "Contact us")
        self.sing_in_button = (By.LINK_TEXT, "Sign in")
        self.searchbox = (By.ID, "search_query_top")
        self.submit_button = (By.NAME, "submit_search")

    def contact_button_click(self):

        self.driver.find_element(*self.contact_button).click()

    def sign_in_button_click(self):

        self.driver.find_element(*self.sing_in_button).click()

    def searchbox_search_word(self, item):

        self.driver.find_element(*self.searchbox).send_keys(item) 
        self.driver.find_element(*self.submit_button).click()   









