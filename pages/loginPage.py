
from pages.base_pages import BasePage


class LoginPage(BasePage):
    URL="https://www.saucedemo.com"
    USERNAME_INPUT="#user-name"
    PASSWORD_INPUT="#password"
    LOGIN_BUTTON="#login-button"
    ERROR_MESSAGE="[data-test='error']"
    
 
        
    def open(self):
        """abre la página de login"""
        self.navigate()
        

    def login(self, usuario, clave):
        """TODO: llena usuario, llena clave, click en el botón.
        Son las 3 líneas que ya escribiste en tus tests,
        pero usando self.page y las constantes de arriba."""
        self.page.fill(self.USERNAME_INPUT, usuario)
        self.page.fill(self.PASSWORD_INPUT, clave)
        self.page.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        return self.page.text_content(self.ERROR_MESSAGE)
    
        



        

    