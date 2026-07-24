

from tkinter import SEL

from pages.base_pages  import BasePage

class InventoryPage(BasePage):
  
    INVENTORY_ITEM=".inventory_item"
    CAR_BUTTON="a.shopping_cart_link"
    
    def count_products(self):
        return self.page.locator(self.INVENTORY_ITEM).count()
    
    def go_to_cart(self):
        self.page.click(self.CAR_BUTTON)
    
    def add_product_to_cart(self, product_name):
        """agrega un producto al carrito, dado su nombre"""
        product_id= product_name.lower().replace(" ", "-")
        self.page.click(f"button[data-test='add-to-cart-{product_id}']")
        
   
        