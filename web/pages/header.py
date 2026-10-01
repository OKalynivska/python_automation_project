import allure

from web.locators.navbar_locators import NavBarLocator
from web.pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Click on 'Cart' button")
    def click_on_cart_button(self):
        role, name = NavBarLocator.CART_LINK.value
        self.page.get_by_role(role, name=name).click()

    @allure.step("Click on 'Test Cases' button")
    def click_on_test_cases_button(self):
        role, name = NavBarLocator.TEST_CASES_LINK.value
        self.page.get_by_role(role, name=name).click()