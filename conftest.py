import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD


web_app = "https://www.saucedemo.com/"


@pytest.fixture
def logged_in_page(page: Page):
    page.goto(web_app)
    LoginPage(page).login(USERNAME, PASSWORD)
    return page
