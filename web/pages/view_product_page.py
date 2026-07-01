import allure
from playwright.sync_api import expect

from web.pages.base_page import BasePage


class ViewProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Assert redirect 'View Product page'")
    def assert_view_product_page_redirect(self, id):
        expect(self.page).to_have_url(f'https://automationexercise.com/product_details/{id}'), "Url is not correct"