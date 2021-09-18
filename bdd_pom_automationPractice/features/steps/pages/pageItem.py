from selenium.webdriver.common.by import By


class PageItem(object):

    def __init__(self, my_driver):

        self.driver = my_driver
        self.title = (By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/h1/span[1]")

    def title_text(self):

        return self.driver.find_element(*self.title).text

         

       
 
