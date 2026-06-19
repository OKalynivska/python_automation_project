import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Navigate to page '{url}'")
    def navigate(self, url: str):
        self.page.goto(url)