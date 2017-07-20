from  base.selenium_webdriver import MyDriver

class Base_page(MyDriver):
    """
    This class inherits MyDriver and every other modules in the framework should inherit Base Page to access My Driver.
    
    This class provides the common methods that are used in all the pages. 
    
    """
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def verify_title(self,actual_title,expected_title):
        pass


    def exittest(self):
        self.driver.close()
        print("driver closed after test")