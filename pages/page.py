import allure
from selene import browser, have, be


class StartPage:
    def __init__(self):
        self.button_sing_in_desktop=browser.element('.HeaderMenu-link--sign-in')
        self.button_sing_in_mobile=browser.element('.HeaderMenu-link[href="/login"]')

    @allure.step('Открываем главную страницу Github')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Кликаем по кнопке Sing In в десктопной версии')
    def click_desktop(self):
        self.button_sing_in_desktop.click()
        return self

    @allure.step('Проверяем, что произошел переход на страницу логина')
    def expect_page_login(self):
        browser.should(have.url('https://github.com/login'))
        browser.should(have.title('Sign in to GitHub · GitHub'))
        return self

    @allure.step('Кликаем по кнопке Sing In в мобильной версии')
    def click_mobile(self):
        self.button_sing_in_mobile.click()
        return self