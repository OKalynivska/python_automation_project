import random

import allure
from playwright.sync_api import expect

from web.locators.home_locators import HomeLocators
from web.locators.navbar_locators import NavBarLocator
from web.pages.base_page import BasePage


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

    @allure.step("Click on 'View product' button")
    def click_on_view_product(self, random_index):
        buttons = self.page.locator(HomeLocators.VIEW_PRODUCT_BUTTONS)
        buttons.nth(random_index-1).click()
        return self
