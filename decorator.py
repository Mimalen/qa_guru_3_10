import functools

import pytest
from allure import step
from selene.support.shared import browser
from selenium.webdriver import Edge


@pytest.fixture
def setup_browser():
    # browser.set_driver(Edge())
    browser.config.driver = Edge()
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

# @allure.tag('web')
# @allure.label('owner', 'Mimalen')
# @allure.severity(Severity.NORMAL)
# @allure.feature('Check the task')
# @allure.story('Decorator')
# @allure.link('https://demoqa.com/automation-practice-form', name='test_decorator')
# def test_decorator():
#     browser.config.driver = Edge()
#     open_main_page()
#     search_repository('eroshenkoam/allure-example')
#     open_repository('eroshenkoam/allure-example')
#     open_issue()
#     check_repository('#76')
#
#
# @allure.step('Open the main page')
# def open_main_page():
#     browser.open('https://github.com/')
