from selenium.webdriver.common.by import By


class PageAll(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.dropdown = (By.ID, 'segmentMenu')
        self.dropdown_eminent = (By.LINK_TEXT, 'Éminent')
        self.sucursales_link = (By.ID, "sucursales-y-cajeros") 
        self.menu = (By.ID, "dropdownMenu")        

    def dropdown_click(self):

        self.driver.find_element(*self.dropdown).click()

    def dropdown_eminent_click(self):

        self.driver.find_element(*self.dropdown_eminent).click()

    def sucursalesYCajeros_link_click(self):

        self.driver.find_element(*self.sucursales_link).click()
   
    def menu_click(self):

        self.driver.find_element(*self.menu).click()

    
    



