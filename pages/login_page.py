from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in str(self.browser.current_url), "This is not login link!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Not found login form on page!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Not found register form on page!"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field_first = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD_FIRST)
        pass_field_first.send_keys(password)
        pass_field_sec = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD_SEC)
        pass_field_sec.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()


