from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")
    NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    COST_IN_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")

