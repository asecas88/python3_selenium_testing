from selenium.webdriver.common.by import By


class PageAppGalicia(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.get_button = (By.XPATH, "/html/body/div[5]/div[3]/div/div[4]/div/div[1]/div/section/div[2]/div[2]/div/div[1]/div/div/div/div/a[1]/img")
        self.download_button = (By.XPATH, "/html/body/div[5]/div[3]/div/div[4]/div/div[1]/div/section/div[2]/div[2]/div/div[1]/div/div/div/div/a[2]/img")
        
    def find_get_button(self):

        return self.driver.find_element(*self.get_button).is_displayed()

    def find_download_button(self):

        return self.driver.find_element(*self.download_button).is_displayed()
