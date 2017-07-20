from base.basepage import Base_page
from selenium.webdriver.common.keys import Keys
from time import sleep
from utilities.test_status import Test_Status



class CoursePage(Base_page):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver




# Navigator Bar Element and Locator List
    _locator_ui, _usericon = 'xpath',"//ul[@class='nav navbar-nav navbar-right']//li[4]"

#Courese page Elements and Locator List
    _locator_fctf,_find_course_text_field= "#search-courses","css selector"
#Selenium Web driver Bundle (Java+Python)
    _locator_full_Course,_locator_type_python_java='//div[@data-course-id={0}]','xpath'
# # Enroll in Course Button (Common ID) Course detail page
    _Locator_Enroll_course,_locator_type_enroll_course= 'enroll-button-top','id'
# Credit Card Elements
    _Locator_card_number,_locator_type_card_number='cc_field','id'
    _locator_expir_field,_locator_type_expir_field='cc-exp','id'
    _locator_cvc_code,_locator_Type_ccv_code='cc_cvc','id'
    _locator_country,_locator_type_country='country-select-inside','id'
    _locator_verify_cc_butn,_locator_type_verify_cc_buttn='verify_cc_btn','id'

# Assertion elements:
    _locator_incorrect_card,locator_type_incorrect_card='//div[@class="payment-errors invalid_number"] [contains(text(),"The card number is invalid.")]','xpath'

# Logo Button
    _logo_locator,_logo_locator_Type="//span[@class='sr-only'][contains(text(),'Kode')]//following-sibling::img",'xpath'
#Logout Button
    _logout_locator,_logout_locator_type="//ul[@class='nav navbar-nav navbar-right']//following-sibling::li[4][@class='dropdown']","xpath"

    _logout_link_locator,_logout_link_locator_type="//ul[@class='dropdown-menu']/li[4]/a[contains(text(),'Log Out')]",'xpath'


####COMMON METHODS#########
    # use it to click the course. Enter locator and locator type while using it in test steps
    def select_click_element(self, locator, locatorType):
        self.clickElement(locator, locatorType)
    def select_dropdown_element(self, locator, locatorType, select_by_type, select_by_entry):
        self.select_option(locator, locatorType, select_by_type, select_by_entry)
# PAGE ACTIONS

#Finding course search field and entering search data and clicking enter.

    def SearchField_Enter(self,data):
        self.sendData(data,self._locator_fctf,self._find_course_text_field).send_keys(Keys.ENTER)

# Select the course out of searched keyword

    def Slect_Searched_Course(self,course_ID):
        self.clickElement(self._locator_full_Course.format(course_ID),self._locator_type_python_java)

# Select Enroll Course button once the selected course detail page loaded
    def click_Enroll_button(self):
        self.clickElement(self._Locator_Enroll_course,self._locator_type_enroll_course)

# Credit Card details
    def enter_credit_card_number(self,cc_num):
        self.sendData_No_clear(cc_num,self._Locator_card_number,self._locator_type_card_number)
    def enter_Exp_date(self,exp_date):
        self.sendData_No_clear(exp_date,self._locator_expir_field,self._locator_type_expir_field)
    def enter_cvv_number(self,cvv_num):
        self.sendData_No_clear(cvv_num,self._locator_cvc_code,self._locator_Type_ccv_code)

    def select_country(self,select_by_type, select_by_entry):
        self.select_option(self._locator_country,self._locator_type_country, select_by_type, select_by_entry)
    def verify_CCDetails_button(self):
        self.clickElement(self._locator_verify_cc_butn,self._locator_type_verify_cc_buttn)

    #Assert section
    def assert_course_page(self):
        result=self.new_Assert_check(self.locator_type_incorrect_card,self._locator_incorrect_card)
        return result

    #Scroll UP course page:
    def scroll_UP_CP(self,scroll_value):
        self.scrollup(scroll_value)

    def click_Logo_CP(self):
        self.clickElement(self._logo_locator,self._logo_locator_Type)

    def click_logout_Button_CP(self):
        self.clickElement(self._logout_locator,self._logout_locator_type)

    def click_logout_drdwn_option(self):
        self.clickElement(self._logout_link_locator,self._logout_link_locator_type)

    def click_logout_CP_summed(self):
        self.click_logout_Button_CP()
        sleep(2)
        self.click_logout_drdwn_option()




# Credit Card Selection Summed up

    def credit_Card_Details_Summed_UP(self,cc_num,exp_date,cvv_num,select_by_type, select_by_entry):
        self.enter_credit_card_number(cc_num)
        self.enter_Exp_date(exp_date)
        self.enter_cvv_number(cvv_num)
        self.select_country(select_by_type, select_by_entry)


    # def test_invalid_course_boking_course_page(self):
    #     self.SearchField_Enter('python')
    #     self.Slect_Searched_Course('154615')
    #     self.click_Enroll_button()
    #     self.credit_Card_Details_Summed_UP('5555','0212','589','value','IN')
    #     self.verify_CCDetails_button()
    #     result=self.assert_course_page()
    #     print(result)
    #     self.ts.mark_final(result,'test_invalid_course_booking','checking course enrollment')















