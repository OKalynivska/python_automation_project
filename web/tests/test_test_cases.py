import allure

from web.pages.test_cases_page import TestCasesPage


class TestTestCases:
    @allure.title("Test Cases elements present - positive scenario")
    def test_cases_elements_present(self, header, test_cases):
        header.click_on_test_cases_button()
        test_cases.assert_test_cases_elements_are_present()
