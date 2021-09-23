from selenium.webdriver.common.by import By


class PageTarjetas(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div[5]/div[3]/div/div[3]/div/div[1]/div/section/div[2]/div[2]/div/section[1]/div/div/div/div/div/div[2]/h1")
        self.sacaTuTarjeta_button = (By.XPATH, "/html/body/div[5]/div[3]/div/div[3]/div/div[1]/div/section/div[2]/div[2]/div/section[1]/div/div/div/div/div/div[2]/a")

    def title_text(self):

        return self.driver.find_element(*self.title).text

    def find_sacaTuTarjeta_button(self):

        return self.driver.find_element(*self.sacaTuTarjeta_button).is_displayed()
