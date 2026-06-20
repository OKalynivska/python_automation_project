import allure

from pages import login_page


class TestLogin:

  @allure.step
  def test_click_signup_link(self, login_page):
    login_page.click_signup()
