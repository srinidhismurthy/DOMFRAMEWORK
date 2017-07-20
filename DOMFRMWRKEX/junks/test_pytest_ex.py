from selenium import webdriver
import pytest
from page.home.login_page import LoginPage as LP
@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    baseURL = "https://letskodeit.teachable.com/"
    driver.get(baseURL)
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test1_validlogin(setup):

    lp = LP(setup)
    lp.loginsuccess('test@gmail.com', 'abcabc')

def test2_invalid(setup):
    lp = LP(setup)
    lp.loginfail1('tes@gmail.com', 'password')
