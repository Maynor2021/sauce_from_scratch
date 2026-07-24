

from pages.base_pages import BasePage


class CartPage(BasePage):
    
    CART_ITEM = ".cart_item "
    CHECKOUT_BUTTON = "button#checkout"
    ITEM_NAME=".inventory_item_name"


    def count_items(self):
        """retorna la cantidad de items en el carrito"""
        return self.page.locator(self.ITEM_NAME).count()
    
    def get_item_names(self):
        """retorna una lista con los nombres de los items en el carrito"""
        item_names = []
        for i in range(self.count_items()):
            item_names.append(self.page.locator(self.ITEM_NAME).nth(i).text_content())
        
        return item_names
    
    def click_checkout(self):
        """click en el botón de checkout"""
        self.page.click(self.CHECKOUT_BUTTON)
    
    