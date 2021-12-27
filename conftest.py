import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'into.accept_languages': 'en'})
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.quit()
