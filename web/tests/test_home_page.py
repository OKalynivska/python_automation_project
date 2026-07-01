import allure


class TestHomePage:

    @allure.title("Check 'Home page' structure")
    def test_home_page_structure(self, welcome_page, home_page):
        (welcome_page.click_signup()
         .fill_in_email("ta@user")
         .fill_in_password("Password1_")
         .click_login_button())
        home_page.assert_left_sidebar_is_visible()


    @allure.title("Check redirect to 'View product' page")
    def test_redirect_to_view_product_page(self, welcome_page, home_page, view_product_page):
        (welcome_page.click_signup()
         .fill_in_email("ta@user")
         .fill_in_password("Password1_")
         .click_login_button())
        home_page.click_on_view_product(1)
        view_product_page.assert_view_product_page_redirect(1)


