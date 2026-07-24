import pytest

from pages.checkout import CheckoutPage
from pages.cart_page import CartPage




@pytest.mark.regression
def test_checkout(Inventory_page):
    Inventory_page.add_product_to_cart("Sauce Labs Backpack")
    Inventory_page.go_to_cart()
    cart=CartPage(Inventory_page.page)
    cart.click_checkout()
    
    
    
    
    checkout_page=CheckoutPage(Inventory_page.page)
    checkout_page.fill_checkout_info("Maynor", "Rodriguez", "12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    
  
    assert checkout_page.get_confirmation_message() == "Thank you for your order!", f"Expected confirmation message 'Thank you for your order!', but got '{checkout_page.get_confirmation_message()}'"
    
    

    