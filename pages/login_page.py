import allure

from locators.navbar_locators import NavBarLocator
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    @allure.step
    def click_signup(self):
        role, name = NavBarLocator.SIGH_UP_LINK.value
        self.page.get_by_role(role, name=name).click()
        return self