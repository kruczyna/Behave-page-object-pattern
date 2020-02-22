from selenium.webdriver.common.by import By

from features.page_objects.base_page import BasePage


class LoginPage(BasePage):
    # buttons
    login_button = (By.CSS_SELECTOR, '.login')
    submit_login = (By.CSS_SELECTOR, '#SubmitLogin')
    create_account = (By.CSS_SELECTOR, '#SubmitCreate')

    # user fields
    login_field = (By.CSS_SELECTOR, '#email')
    password_field = (By.CSS_SELECTOR, '#passwd')

    # error messages
    invalid_email = (By.XPATH, '//li[contains(text(), "Invalid email address.")]')
    authentication_failed = (By.XPATH, '//li[contains(text(), "Authentication failed.")]')
    email_required = (By.XPATH, '//li[contains(text(), "An email address required.")]')

    def navigate_to_sign_in(self):
        self.visit()
        self.wait_for_element(self.login_button)
        self.find_element(*self.login_button).click()
        assert "controller=authentication" in self.get_current_url()

    def submit_login_form(self, login, password):
        self.wait_for_element(self.login_field)
        self.find_element(*self.login_field).send_keys(login)
        self.find_element(*self.password_field).send_keys(password)
        self.find_element(*self.submit_login).click()

    def login_form_error(self, error_message: str):
        error_messages = {
            "invalid email address": self.invalid_email,
            "authentication failed": self.authentication_failed,
            "email address required": self.email_required
        }
        self.wait_for_element(error_messages[error_message])
        self.browser.find_element(*error_messages[error_message])
