from selenium import webdriver                                     # (must install selenium library)
import unittest

from pages.pageAll import PageAll
from pages.pagePersonas import PagePersonas
from pages.pageLogin import PageLogin
from pages.pageSucursalesYCajeros import PageSucursalesYCajeros
from pages.pageCobraConNosotros import PageCobraConNosotros
from pages.pageHaceteGalicia import PageHaceteGalicia
from pages.pageTurnosSucursales import PageTurnosSucursales
from pages.pageTarjetas import PageTarjetas
from pages.pageInversiones import PageInversiones
from pages.pageSeguros import PageSeguros
from pages.pageCuentaClassic import PageCuentaClassic
from pages.pageAppGalicia import PageAppGalicia


class Galicia(unittest.TestCase):

    def setUp(self):                                        
                     # Firefox webdriver                         configurate webdriver dir   
        self.driver = webdriver.Firefox(executable_path= r"/your webdriver dir.../driverFirefox")
        self.driver.get("https://www.bancogalicia.com/banca/online/web/Personas")
        self.driver.implicitly_wait(5)

        self.pageAll = PageAll(self.driver)
        self.pagePersonas = PagePersonas(self.driver)
        self.pageLogin = PageLogin(self.driver)
        self.pageSucursales = PageSucursalesYCajeros(self.driver)
        self.pageCobra = PageCobraConNosotros(self.driver)
        self.pageHaceteGalicia = PageHaceteGalicia(self.driver)
        self.pageTurnosSucursales = PageTurnosSucursales(self.driver)
        self.pageTarjetas = PageTarjetas(self.driver)
        self.pageInversiones = PageInversiones(self.driver)
        self.pageSeguros = PageSeguros(self.driver)
        self.pageClassic = PageCuentaClassic(self.driver)
        self.pageAppGalicia = PageAppGalicia(self.driver)
    #
    def test_onlineBanking_button(self):

        self.pagePersonas.onlineBanking_button_click()

        self.assertTrue("Iniciar sesión" in self.pageLogin.title_text())
    #
    def test_dropdown_eminent(self):

        self.pageAll.dropdown_click()
        self.pageAll.dropdown_eminent_click()    
    # 
    def test_sucursalesYCajeros_link(self):

        self.pageAll.sucursalesYCajeros_link_click()

        self.assertTrue("Encontrá la opción más cercana" in self.pageSucursales.title_text())
    #
    def test_cobrarSueldoEnGalicia_link(self):
      
        self.pagePersonas.cobrarSueldoEnGalicia_link_click()

        self.assertTrue(self.pageCobra.find_quieroSerCliente_button())
        self.assertTrue(self.pageCobra.find_yaSoyCliente_button())
    #
    def test_haceteGalicia_link(self):

        self.pagePersonas.haceteGalicia_link_click()

        self.assertTrue("Hacete Galicia" in self.pageHaceteGalicia.title_text())
    #
    def test_turnosSucursales_link(self):

        self.pagePersonas.turnosSucursales_link_click()

        self.assertTrue("Reservá turno" in self.pageTurnosSucursales.title_text()) 
        self.assertTrue(self.pageTurnosSucursales.find_sacarTurno_button1())      
        self.assertTrue(self.pageTurnosSucursales.find_sacarTurno_button2())
    #  
    def test_menu_todasLasTarjetas_link(self):

        self.pageAll.menu_click()
        self.pagePersonas.menu_todasLasTarjetas_click()

        self.assertTrue("Tarjetas Galicia" in self.pageTarjetas.title_text())
        self.assertTrue(self.pageTarjetas.find_sacaTuTarjeta_button())
    
    def test_menu_todasLasInversiones_link(self):

        self.pageAll.menu_click()
        self.pagePersonas.menu_todasLasInversiones_click()

        self.assertTrue("Inversiones Galicia" in self.pageInversiones.title_text())
        self.assertTrue(self.pageInversiones.find_invertir_button())
    
    def test_menu_todosLosSeguros_link(self):

        self.pageAll.menu_click()
        self.pagePersonas.menu_todosLosSeguros_click()

        self.assertTrue("Seguros para vos" in self.pageSeguros.title_text())
    
    def test_menu_cuentaClassic(self): 

        self.pageAll.menu_click()
        self.pagePersonas.menu_cuentaClassic_click()

        self.assertTrue("SERVICIO GALICIA CLASSIC" in self.pageClassic.title_text())
    
    def test_menu_appGalicia(self):

        self.pageAll.menu_click()
        self.pagePersonas.menu_appGalicia_click()

        self.assertTrue(self.pageAppGalicia.find_get_button())
        self.assertTrue(self.pageAppGalicia.find_download_button())
    #
    def tearDown(self):

        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')







