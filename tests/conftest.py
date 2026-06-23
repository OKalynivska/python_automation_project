import pytest
from playwright.sync_api import sync_playwright

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

@pytest.fixture
def welcome_page(page):
    return WelcomePage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)
