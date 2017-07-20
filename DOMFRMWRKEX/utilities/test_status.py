from base.basepage import Base_page

class Test_Status(Base_page):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.result=[]


    def setStatus(self,result,testname,testmessage=""):

        try:
            if result is not None:
                if result is True:
                    self.result.append("PASS")
                    self.log.info("###########ASSERTION SUCCEEDED in test{}".format(testname))
                else:
                    self.result.append("FAIL")
                    self.log.info("###########.1 .ASSERTION FAILED in test{}".format(testname))
                    self.Take_Screenshot()
            else:
                self.result.append("FAIL")
                self.log.info("########### 2. ASSERTION FAILED in test{}".format(testname))
                self.Take_Screenshot()
        except:
                self.result.append("FAIL")
                self.log.info("########### 3. SSERTION FAILED in test{}".format(testname))
                self.Take_Screenshot()

    def mark1(self,result,testname,testmessage=""):

        self.setStatus(result,testname,testmessage)


    def mark_final(self,result,testname,testmessage=""):

        self.setStatus(result, testname, testmessage)
        print(self.result)

        if 'FAIL' in self.result:
            print(self.result)
            self.log.error("##TestCase {} Failed as {}##".format(testname,"as Asserion Failed"))

        self.result.clear()



