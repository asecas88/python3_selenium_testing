from selenium.webdriver.common.by import By


class PageCobraConNosotros(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.quieroSerCliente_button = (By.LINK_TEXT, "Quiero ser cliente")
        self.yaSoyCliente_button = (By.LINK_TEXT, "Ya soy cliente")

    def find_quieroSerCliente_button(self):

        return self.driver.find_element(*self.quieroSerCliente_button).is_displayed()
                                 
    def find_yaSoyCliente_button(self):

        return self.driver.find_element(*self.yaSoyCliente_button).is_displayed()
