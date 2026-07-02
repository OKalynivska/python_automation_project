import allure
from playwright.sync_api import expect

from web.locators.view_cart_locators import ViewCartLocators
from web.pages.base_page import BasePage


class ViewCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Assert Product(s) count in Cart: '{number}'")
    def assert_number_of_products(self, number):
        expect(self.page.locator(ViewCartLocators.PRODUCT_ITEMS)).to_have_count(number)