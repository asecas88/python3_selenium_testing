from selenium.webdriver.common.by import By


class PageSeguros(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div[5]/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/section/div[2]/div[2]/div/div/div/section[1]/div/div/div[2]/h1")

    def title_text(self):

        return self.driver.find_element(*self.title).text
