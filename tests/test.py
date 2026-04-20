import allure
import pytest
from selene import browser

from conftest import SIZES
from pages.page import StartPage

page=StartPage()

@allure.title('Базовый десктоп тест')
def test_login_page_desktop():
    (page.open()
     .click_desktop()
     .expect_page_login())

@pytest.mark.parametrize('page_size', SIZES)
@allure.title('Десктоп с параметризацией и скипом модильных соотношений')
def test_login_page_decktop_skip(page_size):
    width, height = page_size
    if width < 1440:
        pytest.skip('Мобильный размер - скипаем в десктоп тесте')

    browser.config.window_width = width
    browser.config.window_height = height

    (page.open()
     .click_desktop()
     .expect_page_login())

@pytest.mark.parametrize('page_size', SIZES)
@allure.title('Базовый мобильный тест')
def test_login_page_mobile_skip(page_size):
    width, height = page_size
    if width > 375:
        pytest.skip('Десктопный размер - скрипаем в мобильном тесте')

    browser.config.window_width = width
    browser.config.window_height = height

    (page.open()
     .click_mobile()
     .expect_page_login())

@pytest.mark.parametrize('set_size_page', [(1920,1080), (1440, 615)], indirect=True)
@allure.title('Десктоп с индиректом')
def test_desktop_indirect(set_size_page):
    (page.open()
     .click_desktop()
     .expect_page_login())

@pytest.mark.parametrize('set_size_page', [(720, 553),(320,550)], indirect=True)
@allure.title('Мобилка с индиректом')
def test_mobile_indirect(set_size_page):
    (page.open()
     .click_mobile()
     .expect_page_login())

@allure.title('Десктоп с отдельной фикстурой')
def test_desktop_indirect(desktop_browser):
    (page.open()
     .click_desktop()
     .expect_page_login())

@allure.title('Мобилка с отдельной фикстурой')
def test_mobile_indirect(mobile_browser):
    (page.open()
     .click_mobile()
     .expect_page_login())