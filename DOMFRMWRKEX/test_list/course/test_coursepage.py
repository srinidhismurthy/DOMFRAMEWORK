import pytest
from page.course.course_page import CoursePage as CP
from utilities.test_status import Test_Status


@pytest.mark.usefixtures('onetime_setup')
class Test_Course_Page():

    @pytest.fixture(autouse=True)
    def classlevel_setup(self,onetime_setup):
        self.cp=CP(self.driver)
        self.ts=Test_Status(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_course_boking(self):
        self.cp.SearchField_Enter('python')
        self.cp.Slect_Searched_Course('154615')
        self.cp.click_Enroll_button()
        self.cp.credit_Card_Details_Summed_UP('5555','0212','589','value','IN')
        self.cp.verify_CCDetails_button()
        result=self.cp.assert_course_page()
        print(result)
        self.ts.mark_final(result,'test_invalid_course_booking','checking course enrollment')

