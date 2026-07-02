import allure
import pytest
from playwright.sync_api import sync_playwright, Page

from web.pages.home_page import HomePage
from web.pages.view_product_page import ViewProductPage
from web.pages.welcome_page import WelcomePage


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
    page.set_viewport_size({"width": 1920, "height": 1280})
    yield page
    page.close()

@pytest.fixture
def logged_in_page(page):
    welcome_page = WelcomePage(page)
    home_page = welcome_page.log_in()
    return home_page

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

@pytest.fixture
def view_product_page(page):
    return ViewProductPage(page)
