import allure

from web.locators.login_locators import LoginLocators
from web.locators.navbar_locators import NavBarLocator
from web.pages.base_page import BasePage


class WelcomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Click on 'Sign up' button")
    def click_signup(self):
        role, name = NavBarLocator.SIGH_UP_LINK.value
        self.page.get_by_role(role, name=name).click()
        return self


    @allure.step("Assert 'Sign in' form present")
    def assert_sign_in_form_present(self):
        assert self.page.locator(LoginLocators.LOGIN_FORM.value).is_visible(), \
            "Sign in form is not visible"
        return self

    @allure.step("Fill in Email field")
    def fill_in_email(self, email: str):
        self.page.locator(LoginLocators.EMAIL.value).fill(email)
        return self

    @allure.step("Fill in Password field")
    def fill_in_password(self, password: str):
        self.page.locator(LoginLocators.PASSWORD.value).fill(password)
        return self

    @allure.step("Click on 'Login' button")
    def click_login_button(self):
        self.page.locator(LoginLocators.LOGIN_BUTTON.value).click()

    @allure.step("Log in")
    def log_in(self, welcome_page, home_page):
        (welcome_page.click_signup()
         .fill_in_email("ta@user")
         .fill_in_password("Password1_")
         .click_login_button())

