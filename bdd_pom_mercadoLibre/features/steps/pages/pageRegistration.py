from selenium.webdriver.common.by import By


class PageRegistration(object):

    def __init__(self, my_driver):

        self.driver = my_driver
        self.title = (By.XPATH, "/html/body/main/div/div/h1")

    def title_text(self):

        return self.driver.find_element(*self.title).text
