from pages.base_page import BasePage
from pages.locators import  BasketPageLocators


class BasketPage(BasePage):

    def check_basket_empty_text(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert basket_text == "Ваша корзина пуста Продолжить покупки", "Problems with basket text)!"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty!"

