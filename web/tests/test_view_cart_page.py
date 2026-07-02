import allure


class TestViewCartPage:
    @allure.title("Check number of products in cart")
    def test_product_number_in_cart(self, home_page, modal_component, view_cart_page):
        home_page.click_on_add_to_cart_button(2)
        modal_component.click_view_cart()
        view_cart_page.assert_number_of_products(1)

