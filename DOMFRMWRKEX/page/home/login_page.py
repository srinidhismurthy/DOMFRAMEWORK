from time import sleep
from base.basepage import Base_page
from utilities.test_status import Test_Status
from Navigation_page.navigation_page import navigation_page_Course as NPC

# ELEMENT SECTION:

class LoginPage(Base_page):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.ts=Test_Status(driver)
        self.npc=NPC(driver)



    #LOGIN Locators
    _loginLink,_locatortype1="xpath","//a[contains(text(),'Login')]"
    _loginTextField,_locatortype2="id","user_email"
    _passwordTextField,_locatortype3="id","user_password"
    _loginConfirmButton,_locatortype4="xpath","//input[@name='commit']"
    _failedloginerror,_locatorytype6="//div[contains(text(),'Invalid')]",'xpath'

    #ELEMETNS FROM OTHER PAGES
    #1.Elements from course page
    # Navigator Bar Element and Locator List
    _usericon, _locatortype5 = "//ul[@class='nav navbar-nav navbar-right']//li[4]", 'xpath'

    # Courese page Elements and Locator List
    _find_course_text_field, _locatortype7 = "#search-courses", "css selector"


    # Login ACTIONS

    def getLoginLink_click(self):
        self.clickElement(self._loginLink,self._locatortype1)

    def getEmailField_EnterID(self,emailID,):
        self.sendData(emailID,self._loginTextField,self._locatortype2)

    def getPasswordField_EnterPassword(self,password):
        self.sendData(password, self._passwordTextField,self._locatortype3)

    def getLoginButton_click(self):
        self.clickElement(self._loginConfirmButton,self._locatortype4)
        sleep(5)

    def getUserIcon(self):
        userIcon = self.getElement(self._usericon, self._locatortype5)
        return userIcon

    def getFailedLoginNote(self):
        loginfailnote=self.getElement(self._failedloginerror,self._locatorytype6)
        sleep(3)
        return loginfailnote


    # STANDARD VALID LOGIN TEST CASE template
    def loginsuccess(self,email,password):

        # Before creating"Individual Elements for tests"
        ######################################################################

        # loginLink = self.getElement(self._loginLink,self._locatortype1)
        # loginLink.click()
        #
        # # Page redirected to login page
        #
        # # Locating Login Text Field
        #
        # loginTextField = self.getElement(self._loginTextField,self._locatortype2)
        # loginTextField.send_keys(username)
        #
        # # Locating Password Field
        # passwordTextField = self.getElement(self._passwordTextField,self._locatortype3)
        # passwordTextField.send_keys(password)
        #
        # # Locate and click on Login Button
        # loginConfirmButton = self.getElement(self._loginConfirmButton,self._locatortype4)
        # loginConfirmButton.click()
        # sleep(5)
        #
        # userIcon = self.getElement(self._usericon,self._locatortype5)
        ##################################################################################
        self.getLoginLink_click()
        self.getEmailField_EnterID(email)
        self.getPasswordField_EnterPassword(password)
        self.getLoginButton_click()

        result1=self.new_Assert_check(self._locatortype5,self._usericon,)
        self.ts.mark1(result1,'test2_validLogin')
        result2=self.new_Assert_check(self._locatortype7,self._find_course_text_field)
        self.ts.mark_final(result2,'Test2_validLogin')

    #STANDARD INVALID LOGIN TEMPLATE
    def loginfail1(self,email,password):

        # Before creating#"Individual Elements for tests"#
        ##############$$$$$$$$$$$$$$$$$$$$$$$$$$$$%%%%%%%%%%%%###############
        # loginLink = self.getElement(self._loginLink,self._locatortype1)
        # loginLink.click()
        #
        # # Page redirected to login page
        #
        # # Locating Login Text Field
        #
        # loginTextField = self.getElement(self._loginTextField,self._locatortype2)
        # loginTextField.send_keys(username)
        #
        # # Locating Password Field
        # passwordTextField = self.getElement(self._passwordTextField,self._locatortype3)
        # passwordTextField.send_keys(password)
        #
        # # Locate and click on Login Button
        # loginConfirmButton = self.getElement(self._loginConfirmButton,self._locatortype4)
        # loginConfirmButton.click()
        # sleep(5)
        #
        # loginfailnote=self.getElement(self._failedloginerror,self._locatorytype6)
        # sleep(3)
        self.npc.click_log_out_Nav()
        self.getLoginLink_click()
        self.getEmailField_EnterID(email)
        self.getPasswordField_EnterPassword(password)
        self.getLoginButton_click()
        self.elemAssert(self._locatorytype6,self._failedloginerror)









