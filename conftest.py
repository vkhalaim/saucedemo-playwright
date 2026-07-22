import pytest
from pages.login_page import Page, LoginPage


@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    LoginPage(page).login("standard_user", "secret_sauce")
    return page
