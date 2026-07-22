import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from config import USERNAME, USERNAME_LOCKED_OUT, PASSWORD

web_app = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (USERNAME_LOCKED_OUT, PASSWORD, "locked out"),
        ("", "", "Username is required"),
        ("", PASSWORD, "Username is required"),
        (USERNAME, "", "Password is required")
    ],
    ids=["locked_out", "empty_credentials", "empty_username", "empty_password"]
)
def test_login_failure_scenarios(page: Page, username, password, expected_error):
    page.goto(web_app)
    login_page = LoginPage(page)
    login_page.login(username, password)

    assert "inventory.html" not in page.url
    assert expected_error in login_page.get_error_message()
