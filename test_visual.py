from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD

web_app = "https://www.saucedemo.com/"


def test_inventory_page_visual(page: Page, assert_snapshot):
    page.goto(web_app)
    LoginPage(page).login(USERNAME, PASSWORD)
    assert_snapshot(page)