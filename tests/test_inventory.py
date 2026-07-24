

import pytest


@pytest.mark.regression
def test_count_products( Inventory_page):
    cantidad=Inventory_page.count_products()
    assert cantidad == 6, f"Expected 6 products, but got {cantidad}"
        