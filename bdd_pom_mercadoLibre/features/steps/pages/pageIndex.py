from selenium.webdriver.common.by import By


class PageIndex(object):

    def __init__(self, my_driver):

        self.driver = my_driver
        self.search_box = (By.NAME, "as_word")
        self.search_box_submit_button = (By.XPATH, "/html/body/header/div/form/button/div")
        self.crea_tu_cuenta_button = (By.LINK_TEXT, "Creá tu cuenta")
        self.ingresa_button = (By.LINK_TEXT, 'Ingresá')
        self.mis_compras_button = (By.LINK_TEXT, 'Mis compras')

    def search_box_find_item(self, item):

        self.driver.find_element(*self.search_box).send_keys(item)
        self.driver.find_element(*self.search_box_submit_button).click()

    def crea_tu_cuenta_button_click(self):

        self.driver.find_element(*self.crea_tu_cuenta_button).click()

    def ingresa_button_click(self):

        self.driver.find_element(*self.ingresa_button).click()

    def mis_compras_button_click(self):

        self.driver.find_element(*self.mis_compras_button).click()









        

