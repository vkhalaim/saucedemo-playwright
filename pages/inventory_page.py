import re
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_item_to_cart(self, item_name: str):
        name_locator = self.page.locator(
            "[data-test='inventory-item-name']",
            has_text=re.compile(f"^{re.escape(item_name)}$"),
        )
        item_container = self.page.locator(".inventory_item").filter(has=name_locator)
        item_container.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()
