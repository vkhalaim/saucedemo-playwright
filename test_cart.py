import pytest
from playwright.sync_api import Page, expect

web_app = "https://www.saucedemo.com/"
login = "standard_user"
password = "secret_sauce"


def test_item_total_is_correct(page: Page, logged_in_page: Page):
    page.goto(web_app)

    # Interact with login form
    page.locator("[data-test='username']").fill(login)
    page.locator("[data-test='password']").fill(password)
    page.locator("[data-test='login-button']").click()

    # items which should be added to cart
    item1 = "Sauce Labs Backpack"
    item2 = "Sauce Labs Bike Light"

    # add items
    page.locator('[data-test="inventory-item-name"]', has_text=item1).click()
    page.locator('[data-test="add-to-cart"]').click()
    page.locator('[data-test="back-to-products"]').click()

    page.locator('[data-test="inventory-item-name"]', has_text=item2).click()
    page.locator('[data-test="add-to-cart"]').click()

    # proceed to cart
    page.locator("[data-test='shopping-cart-link']").click()

    # check that there are 2 items inside cart and they are correct
    all_items_text = page.locator(
            "[data-test='inventory-item-name']"
            ).all_text_contents()
    assert len(all_items_text) == 2
    assert item1 in all_items_text
    assert item2 in all_items_text

    # proceed to checkout
    page.locator("[data-test='checkout']").click()

    # fill form
    last_name = "Doe"
    first_name = "Joe"
    zip_code = "33011"
    page.locator("[data-test='firstName']").fill(first_name)
    page.locator("[data-test='lastName']").fill(last_name)
    page.locator("[data-test='postalCode']").fill(zip_code)
    page.locator("[data-test='continue']").click()

    # check total price is correct
    all_prices_text = page.locator(
        "[data-test='inventory-item-price']"
        ).all_text_contents()

    all_prices_numbers = [
        float(price.replace("$", "")) for price in all_prices_text
        ]

    total_calculated = sum(all_prices_numbers)
    total_parsed = float(page.locator("[data-test='subtotal-label']").text_content().split("$")[1])

    assert total_calculated == pytest.approx(total_parsed, abs=0.01), (
        f"Item total mismatch: expected {total_calculated}, page shows {total_parsed}"
    )
