import allure
from playwright.sync_api import expect

from locators.home_locators import HomeLocators
from locators.navbar_locators import NavBarLocator
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    @allure.step("Assert 'Logout' button is visible")
    def assert_logout_is_visible(self):
        role, name = NavBarLocator.LOGOUT_LINK.value
        expect (self.page.get_by_role(role, name=name)).to_be_visible(), "Logout button is not visible"


    @allure.step("Assert 'Left sidebar' is visible")
    def assert_left_sidebar_is_visible(self):
        expect (self.page.locator(HomeLocators.LEFT_BAR), "Left sidebar is visible")

    @allure.step("Assert 'Left sidebar' is visible")
    def assert_left_sidebar_is_visible(self):
        expect(self.page.locator(HomeLocators.LEFT_BAR), "Left sidebar is visible")
