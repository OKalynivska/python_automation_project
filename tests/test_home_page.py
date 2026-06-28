import allure


class TestHomePage:

    @allure.title("Check 'Home page' structure")
    def test_home_page_structure(self, welcome_page, home_page):
        (welcome_page.click_signup()
         .fill_in_email("ta@user")
         .fill_in_password("Password1_")
         .click_login_button())
        home_page.assert_left_sidebar_is_visible()
