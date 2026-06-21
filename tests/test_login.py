import allure


class TestLogin:

    @allure.title("Sign in form present - positive scenario")
    def test_sign_in_form_present(self, welcome_page):
        (welcome_page.click_signup()
         .assert_sign_in_form_present())

    @allure.title("Log in - positive scenario")
    def test_log_in_positive(self, welcome_page, home_page):
        (welcome_page.click_signup()
         .fill_in_email("ta@user")
         .fill_in_password("Password1_")
         .click_login_button())  # TestAutomation User
        home_page.assert_logout_is_visible()
