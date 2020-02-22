import behave_webdriver
from selenium import webdriver


AVAILABLE_BROWSERS = {
    'chrome': behave_webdriver.Chrome,
    'chrome_headless': behave_webdriver.Chrome.headless,
    'edge': behave_webdriver.Edge,
    'ie': behave_webdriver.Ie,
}


def before_all(context):
    context.driver = webdriver.Chrome(
        executable_path='/usr/local/bin/chromedriver'
    )


def after_all(context):
    context.driver.quit()
