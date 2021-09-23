from selenium.webdriver.common.by import By


class PagePersonas(object):

    def __init__(self, my_driver):

        self.driver = my_driver

        self.onlineBanking_button = (By.LINK_TEXT, "Online Banking")      
        self.cobrarSueldo_link = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/ul[1]/li[2]/a")
        self.haceteGalicia_link = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/ul[1]/li[3]/a")
        self.turnosSucursales_link = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/ul[1]/li[4]/a")
        self.menu_todasLasTarjetas = (By.LINK_TEXT, "Todas las tarjetas")
        self.menu_todasLasInversiones = (By.LINK_TEXT, "Todas las inversiones")
        self.menu_todosLosSeguros = (By.LINK_TEXT, "Todos los seguros")
        self.menu_cuentaClassic = (By.LINK_TEXT, "Cuenta Classic")
        self.menu_appGalicia = (By.LINK_TEXT, "App Galicia")
        
    def onlineBanking_button_click(self):

        self.driver.find_element(*self.onlineBanking_button).click()
    
    def cobrarSueldoEnGalicia_link_click(self):

        self.driver.find_element(*self.cobrarSueldo_link).click()  

    def haceteGalicia_link_click(self):  

        self.driver.find_element(*self.haceteGalicia_link).click()

    def turnosSucursales_link_click(self):

        self.driver.find_element(*self.turnosSucursales_link).click()
    #
    def menu_todasLasTarjetas_click(self):

        self.driver.find_element(*self.menu_todasLasTarjetas).click()

    def menu_todasLasInversiones_click(self):

        self.driver.find_element(*self.menu_todasLasInversiones).click()

    def menu_todosLosSeguros_click(self):

        self.driver.find_element(*self.menu_todosLosSeguros).click() 

    def menu_cuentaClassic_click(self):  

        self.driver.find_element(*self.menu_cuentaClassic).click() 

    def menu_appGalicia_click(self):

        self.driver.find_element(*self.menu_appGalicia).click()




    





