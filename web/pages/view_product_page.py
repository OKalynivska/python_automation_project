import allure
from playwright.sync_api import expect

from web.locators.view_product_locators import ViewProductLocators
from web.pages.base_page import BasePage


class ViewProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Assert redirect 'View Product page'")
    def assert_view_product_page_redirect(self, id):
        expect(self.page).to_have_url(f'https://automationexercise.com/product_details/{id}'), "Url is not correct"

    @allure.step("Check 'View Product page' structure")
    def assert_view_product_page_structure(self):
        expect(self.page.locator(ViewProductLocators.IMAGE)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.PRODUCT_INFO_BLOCK)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.PRODUCT_QUANTITY)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.PRODUCT_INFO_TITLE)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.ADD_TO_CART_BUTTON)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.EMAIL_INPUT_FIELD)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.NAME_INPUT_FIELD)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.REVIEW_TEXTAREA_FIELD)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.PRODUCT_INFO_CATEGORIES)).to_contain_text(["Category", "Availability", "Condition", "Brand"])
        expect(self.page.locator(ViewProductLocators.SHOP_DETAILS_TAB)).to_be_visible()
        expect(self.page.locator(ViewProductLocators.SUBMIT_BUTTON)).to_be_visible()


    @allure.step("Click on 'Add to cart' button")
    def click_add_to_cart(self):
        self.page.locator(ViewProductLocators.ADD_TO_CART_BUTTON).click()
