import allure
from playwright.sync_api import expect

from locators.navbar_locators import NavBarLocator
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    @allure.step("Assert 'Logout' button is visible")
    def assert_logout_is_visible(self):
        role, name = NavBarLocator.LOGOUT_LINK.value
        expect (self.page.get_by_role(role, name=name)).to_be_visible(), "Logout button is not visible"

