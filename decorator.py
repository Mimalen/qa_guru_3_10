import functools

import pytest
from allure import step
from selene.support.shared import browser
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}


@pytest.fixture
def setup_browser():
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)
    # browser.set_driver(Edge())
    browser.config.driver = driver
    browser.config.window_height = 800
    browser.config.window_width = 1200
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
    browser.open('/automation-practice-form')
    yield browser


def handle_test_with_allure(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        with step(func.__name__):
            func(*args, **kwargs)

    return wrapper_func

