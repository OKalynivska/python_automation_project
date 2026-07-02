import allure


class TestViewProductPage:

   @allure.title("Check ' View Product page' structure")
   def test_view_product_page_structure(self, home_page, view_product_page):
      home_page.click_on_view_product(2)
      view_product_page.assert_view_product_page_structure()
