from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def check_add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        BasePage.solve_quiz_and_get_code(self)

    def check_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.NAME_IN_ALERT).text
        assert product_name == alert_name, "The name of the item in the cart is not equal to the original name of the " \
                                           "item "

    def check_basket_cost(self):
        basket_cost = self.browser.find_element(*ProductPageLocators.COST_IN_ALERT).text
        alert_cost = self.browser.find_element(*ProductPageLocators.COST_IN_ALERT).text
        assert basket_cost == alert_cost, "The value of the basket is not equal to the value of the item "
