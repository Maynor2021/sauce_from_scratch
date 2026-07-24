import pytest 
from pages.loginPage import LoginPage

from pages.inventory_page import InventoryPage

from pathlib import Path

@pytest.fixture
def login_page(page):
    """retorna un loginPage ya baierto en saucedemo.com"""
    lp=LoginPage(page)
    lp.open()
    return lp
@pytest.fixture
def Inventory_page(login_page,):
   """hace login con usiairo valido  y retornna el inventory page"""
   login_page.login("standard_user", "secret_sauce")
   return InventoryPage(login_page.page)

def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        
        page = item.funcargs.get("page")
       
        if page:
            Path("screenshots").mkdir(exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")
            print(f"🔍 Screenshot guardado")