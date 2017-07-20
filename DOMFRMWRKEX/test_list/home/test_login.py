import pytest
from page.home.login_page import LoginPage as LP
from Navigation_page.navigation_page import navigation_page_Course as NPC
from utilities.test_status import Test_Status as TS


@pytest.mark.usefixtures("onetime_setup")
class Test_login():

    @pytest.fixture(autouse=True)
    def classlevelsetup(self,onetime_setup):
        self.lp=LP(self.driver)
        self.npc=NPC(self.driver)
        self.ts=TS(self.driver)

    @pytest.mark.skip
    def test2_validLogin(self):

        self.lp.loginsuccess('test@gmail.com','abcabc')

    @pytest.mark.run(order=1)
    def test1_invalid1(self):
        self.npc.click_log_out_Nav()
        sleep(3)
        self.lp.getLoginLink_click()
        self.lp.getEmailField_EnterID('tes@gmail.com')
        self.lp.getLoginButton_click()
        result=self.lp.new_Assert_check(self.lp._failedloginerror,self.lp._locatorytype6)
        self.ts.mark_final(result,'test1_invalid1')















