import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse='True')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto("https://automationexercise.com")
    yield page
    page.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)
