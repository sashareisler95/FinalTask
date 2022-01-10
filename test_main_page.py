import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/"])
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        link_login = browser.current_url
        login_page = LoginPage(browser, link_login)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.check_basket_empty_text()
    basket_page.is_basket_empty()
