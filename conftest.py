import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_window_height_width():
    browser.config.base_url='https://google.com'
    browser.config.window_height = 1024
    browser.config.window_width = 868
    yield
    browser.quit()

