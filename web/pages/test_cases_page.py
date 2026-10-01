import allure
from playwright.sync_api import expect

from web.locators.test_cases_locators import TestCasesLocators
from web.pages.base_page import BasePage


class TestCasesPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Assert 'Test Cases' elements are present")
    def assert_test_cases_elements_are_present(self):
        expect(self.page.locator(TestCasesLocators.TEST_CASES_HEADER)).to_be_visible()
        expect(self.page.locator(TestCasesLocators.TEST_CASES_NAMES)).not_to_have_count(0)
        expect(self.page.locator(TestCasesLocators.FEEDBACK_TABLE)).to_be_visible()
