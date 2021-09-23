from selenium.webdriver.common.by import By


class PageTurnosSucursales(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.title = (By.XPATH, "/html/body/div[5]/div[3]/div/div[4]/div/div[1]/div[1]/section/div[2]/div[2]/div/section[1]/div/h1")
        self.sacarTurno_button1 = (By.XPATH, "/html/body/div[5]/div[3]/div/div[4]/div/div[1]/div[1]/section/div[2]/div[2]/div/section[1]/div/div[3]/div[1]/div/a")
        self.sacarTurno_button2 = (By.XPATH, "/html/body/div[5]/div[3]/div/div[4]/div/div[1]/div[1]/section/div[2]/div[2]/div/section[1]/div/div[3]/div[2]/div/a")    

    def title_text(self):

        return self.driver.find_element(*self.title).text  

    def find_sacarTurno_button1(self):

        return self.driver.find_element(*self.sacarTurno_button1).is_displayed()  

    def find_sacarTurno_button2(self):

        return self.driver.find_element(*self.sacarTurno_button2).is_displayed()

