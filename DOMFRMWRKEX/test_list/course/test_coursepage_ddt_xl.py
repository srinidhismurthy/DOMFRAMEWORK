import pytest
from page.course.course_page import CoursePage as CP
from utilities.test_status import Test_Status
from ddt import ddt,data,unpack
from time import sleep
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from utilities.read_xls import read_xl
from Navigation_page.navigation_page import navigation_page_Course as NPC

@pytest.mark.usefixtures('onetime_setup')
@ddt
class Test_Course_Page(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classlevel_setup(self,onetime_setup):
        self.cp=CP(self.driver)
        self.ts=Test_Status(self.driver)
        self.npc=NPC(self.driver)


    def setUp(self):
        self.npc.click_Logo_Nav()

    def tearDown(self):
        self.npc.click_Logo_Nav()


    @pytest.mark.run(order=1)
    @data(*read_xl('my_xl.xlsx','Sheet1'))
    @unpack
    def test_invalid_course_booking(self,data,course_ID,cc_num,exp_date,cvc_num,
                                   select_by_type, select_by_entry):
        self.cp.SearchField_Enter(data)
        self.cp.Slect_Searched_Course(course_ID)
        self.cp.click_Enroll_button()
        self.cp.credit_Card_Details_Summed_UP(cc_num,exp_date,cvc_num,
                                   select_by_type, select_by_entry)
        self.cp.verify_CCDetails_button()
        result=self.cp.assert_course_page()
        print(result)
        sleep(3)
        self.ts.mark_final(result,'test_invalid_course_booking')
        print(" Is this getting printed???")
        self.cp.scroll_UP_CP('1000')
        sleep(2)





