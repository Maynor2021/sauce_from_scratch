
class BasePage:
  
    """clase padre de todas las páginas."""
    BASE_URL = "https://www.saucedemo.com"
    def __init__(self, page):
        self.page = page
    
    def navigate(self,path=""):
        """navega a la URL base + path"""
        self.page.goto(f"{self.BASE_URL}{  path}")
        
    def get_title(self):
        """retorna el título de la página"""
        return self.page.text_content(".title")  
    
    

    