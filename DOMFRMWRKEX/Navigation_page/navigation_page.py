from base.basepage import Base_page

class navigation_page_Course(Base_page):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    ####################################################
    ##########LOCATORS and LOCATOR TYPES################
    ####################################################

# My Courses
    _logo_locator,_logo_locator_Type = "//span[@class='sr-only'][contains(text(),'Kode')]//following-sibling::img", 'xpath'
    _my_courses_locator,_mycourse_locator_type='//a[@class="fedora-navbar-link navbar-link"][contains(text(),"My Courses")]','xpath'
    _all_course_locator,all_courses_locator_type='//a[@class="fedora-navbar-link navbar-link current-page"][contains(text(),"All Courses")]','xpath'
    _practice_locator,_practice_locator_type= '//a[@class="fedora-navbar-link navbar-link"][contains(text(),"Practice")]','xpath'
    _logout_locaotr,_logout_locaotr_type="//ul[@class='dropdown-menu']/li[4]/a[contains(text(),'Log Out')]",'xpath'

    ####################################################
    ################!!!PAGE ACTIONS!!!##################
    ####################################################

    def click_Logo_Nav(self):
        self.clickElement(self._logo_locator,self._logo_locator_Type)

    def click_My_Courses_Nav(self):
        self.clickElement(self._my_courses_locator,self._mycourse_locator_type)

    def click_All_Courses_Nav(self):
        self.clickElement(self._all_course_locator,self.all_courses_locator_type)

    def click_All_Practice_Nav(self):
        self.clickElement(self._practice_locator,self._practice_locator_type)

    def click_log_out_Nav(self):
        self.clickElement(self._logout_locaotr,self._logout_locaotr_type)



