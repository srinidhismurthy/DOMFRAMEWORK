from selenium import webdriver
# import test_list.test_junk as TL
#
# class LoggerDemo():
#
#     log=TL.consoleLogger()
#     def methodA(self):
#         self.log.info("THis is an info")
#         self.log.warning("This is warning")
#         self.log.critical("This is crititcal")
#         self.log.error("This is error")
#         self.log.info("This is info")
#
# demo=LoggerDemo()
# demo.methodA()

driver=webdriver.Firefox()

driver.save_screenshot()

