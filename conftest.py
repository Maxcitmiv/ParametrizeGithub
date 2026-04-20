import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_config():
    browser.config.base_url='https://github.com'

SIZES = [(1920, 1080),
         (1440, 615),
         (375, 553),
         (320,550)]

DESKTOP_SIZE = [(1920, 1080), (1440, 615)]
MOBILE_SIZE = [(375, 553), (320,550)]

@pytest.fixture()
def set_size_page(request):
    width, height = request.param

    browser.config.window_width = width
    browser.config.window_height = height

@pytest.fixture(params=DESKTOP_SIZE)
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

@pytest.fixture(params=MOBILE_SIZE)
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height