from selenium.webdriver.common.by import By


class PageInversiones(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div[5]/div[3]/div/div[3]/div/div[1]/div/section/div[2]/div[2]/div/div/section[1]/div/div/div[2]/div/h1")
        self.invertir_button = (By.LINK_TEXT, 'INVERTIR')

    def title_text(self):

        return self.driver.find_element(*self.title).text  

    def find_invertir_button(self):

        return self.driver.find_element(*self.invertir_button).is_displayed()  
