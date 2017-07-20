from selenium import webdriver

class WebDriverFactory():

    def __init__(self,browser):
        self.browser=browser

    def getWebdriverInstance(self):

        driver=None

        if self.browser == "firefox":
            driver = webdriver.Firefox()

        if self.browser == "chrome":
            driver = webdriver.Chrome()

        if self.browser=='ie':
            driver=webdriver.Ie()

        driver.maximize_window()
        baseURL = "https://letskodeit.teachable.com/"
        driver.get(baseURL)
        driver.implicitly_wait(10)
        return driver





