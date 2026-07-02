import allure

from web.locators.modal_locators import ModalLocators
from web.pages.base_page import BasePage


class ModalComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Click on 'View cart' button")
    def click_view_cart(self):
        self.page.locator(ModalLocators.VIEW_CART_LINK).click()
