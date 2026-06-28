import allure
import pytest
from playwright.sync_api import sync_playwright, Page

from pages.home_page import HomePage
from pages.welcome_page import WelcomePage


@pytest.fixture(scope="function", autouse=True)
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto("https://automationexercise.com")
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Page):
    yield
    if request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture
def welcome_page(page):
    return WelcomePage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)
