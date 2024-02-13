import pytest
from selene import browser


@pytest.fixture(scope='function')
def setting_window_height_width():
    browser.config.window_height = 1024
    browser.config.window_width = 868


@pytest.fixture(scope='function')
def open_browser(setting_window_height_width):
    browser.open('https://google.com')
