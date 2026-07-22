import pytest
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


def test_item_total_is_correct(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    item1 = "Sauce Labs Backpack"
    item2 = "Sauce Labs Bike Light"

    inventory_page.add_item_to_cart(item1)
    inventory_page.add_item_to_cart(item2)
    inventory_page.go_to_cart()

    # check that there are 2 items inside cart and they are correct
    all_items_text = logged_in_page.locator(
            "[data-test='inventory-item-name']"
            ).all_text_contents()
    assert len(all_items_text) == 2
    assert item1 in all_items_text
    assert item2 in all_items_text

    # proceed to checkout
    logged_in_page.locator("[data-test='checkout']").click()

    # fill form
    last_name = "Doe"
    first_name = "Joe"
    zip_code = "33011"
    logged_in_page.locator("[data-test='firstName']").fill(first_name)
    logged_in_page.locator("[data-test='lastName']").fill(last_name)
    logged_in_page.locator("[data-test='postalCode']").fill(zip_code)
    logged_in_page.locator("[data-test='continue']").click()

    # check total price is correct
    all_prices_text = logged_in_page.locator(
        "[data-test='inventory-item-price']"
        ).all_text_contents()

    all_prices_numbers = [
        float(price.replace("$", "")) for price in all_prices_text
        ]

    total_calculated = sum(all_prices_numbers)
    total_parsed = float(logged_in_page.locator("[data-test='subtotal-label']").text_content().split("$")[1])

    assert total_calculated == pytest.approx(total_parsed, abs=0.01), (
        f"Item total mismatch: expected {total_calculated}, page shows {total_parsed}"
    )
