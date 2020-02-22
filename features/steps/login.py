from behave import given, use_step_matcher, when

from features.page_objects.login_page import LoginPage

use_step_matcher("re")


@given('I navigate to Sign In form')
def main_page(context):
    page = LoginPage(context.driver)
    page.navigate_to_sign_in()


@when('I submit "([^"]*)" and "([^"]*)"')
def submit_login_form(context, login, password):
    page = LoginPage(context.driver)
    page.submit_login_form(login, password)

