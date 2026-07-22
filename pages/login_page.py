from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.locator("[data-test='username']").fill(username)
        self.page.locator("[data-test='password']").fill(password)
        self.page.locator("[data-test='login-button']").click()

    def get_error_message(self) -> str:
        return self.page.locator("[data-test='error']").text_content()
