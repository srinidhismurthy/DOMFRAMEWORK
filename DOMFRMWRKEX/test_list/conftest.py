import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from page.home.login_page import LoginPage as LP
from page.course.course_page import CoursePage as CP
from time import sleep

@pytest.fixture(scope="class")
def onetime_setup(request,browser):
    print("Running one time setup")

    wdf=WebDriverFactory(browser)
    driver=wdf.getWebdriverInstance()
    lp = LP(driver)
    lp.loginsuccess('test@gmail.com', 'abcabc')

    if request.cls is not None:
        request.cls.driver=driver

    yield driver
    cp=CP(driver)
    cp.click_logout_CP_summed()
    sleep(2)
    driver.close()
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
def osType(request):
    return request.config.getoption("--osType")

# @pytest.fixture(scope='function')
# def testlelevel_setup():
#     cp=CP(self.driver)
#     cp.click_Logo_CP()