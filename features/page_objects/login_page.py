from selenium.webdriver.common.by import By

from features.page_objects.base_page import BasePage


class LoginPage(BasePage):
    login_button = (By.CSS_SELECTOR, '.login')
    submit_login = (By.CSS_SELECTOR, '#SubmitLogin')
    create_account = (By.CSS_SELECTOR, '#SubmitCreate')

    login_field = (By.CSS_SELECTOR, '#email')
    password_field = (By.CSS_SELECTOR, '#passwd')
    user_info = (By.CSS_SELECTOR, '.header_user_info')

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
