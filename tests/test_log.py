import pytest

from pages.loginPage import LoginPage
from playwright.sync_api import expect

@pytest.mark.smoke
def test_login_ll(Inventory_page):
    assert Inventory_page.get_title()=="Products",f"Expected title 'Products', but got '{Inventory_page.get_title()}'"
