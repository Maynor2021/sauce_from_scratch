
import pytest
from pages.cart_page import CartPage


pytest.mark.regression
def test_count_products(Inventory_page):
   Inventory_page.add_product_to_cart("Sauce Labs Backpack")
   Inventory_page.go_to_cart()
   cart=CartPage(Inventory_page.page)
   assert  cart.count_items()==1
   assert "Sauce Labs Backpack" in cart.get_item_names()
   
 

   
   
    