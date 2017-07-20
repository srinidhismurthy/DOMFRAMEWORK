# from selenium import webdriver
# import pytest
# from selenium.webdriver.common.by import By
# from time import sleep
# @pytest.fixture()
# def setUP():
#     # driver = webdriver.Firefox()
#     # driver.maximize_window()
#     # baseURL = "https://letskodeit.teachable.com/"
#     # driver.get(baseURL)
#     # driver.implicitly_wait(10)
#     # yield driver
#     # driver.close()
#     print("I run before all the tests")
#     yield
#     print("I run after all the tests")
#
# @pytest.mark.run(order=2)
# def test_demo1(setUP):
#     # element=setUP.find_element(By.XPATH,"//a[contains(text(),'Login')]" )
#     # element.click()
#     print("I am demo test 1")
# @pytest.mark.run(order=1)
# def test_demo2(setUP):
#     # emailtext=setUP.find_element(By.ID,"user_email")
#     # emailtext.send_keys("test@gmai.com")
#     # sleep(5)
#     print("I am the demo test2")



import os
import time
from base.selenium_webdriver import MyDriver
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('https://letskodeit.teachable.com/')

class Take_Screenshot():

    def create_Folder(self, path, FolderName):

        current_directory = os.getcwd()
        os.chdir(path)
        os.getcwd()
        new_current_directory =os.getcwd()
        print('new_current_directory',new_current_directory)
        new_folder=os.path.join(new_current_directory,FolderName)
        print(new_folder)

        # try:
        if os.path.isdir(new_folder)==True:
            print("path already exists with {}".format(path))
            new_path = os.path.join(path, FolderName)
            os.chdir(new_path)
            final_path = os.getcwd()
            return final_path
        else:
            os.getcwd()
            os.makedirs(FolderName)
            print("Folder Created with FolderName{}".format(FolderName))
            new_path = os.path.join(path,FolderName)
            os.chdir(new_path)
            os.getcwd()
            final_path = os.getcwd()
            return final_path
        # except:
        #     print("Could not create the folder with {0} and {1}".format(path,FolderName))

    def filename_generator(self,prefix,extension):

        filename_generator=str(round(time.time()*1000))
        slice_5letter=filename_generator[:6]
        file_name=prefix+'_'+slice_5letter+extension
        return file_name

    def Take_Screenshot(self,prefix='scrnsht',extension='.png',FolderName='//screenshots',path='C://Users//MEGHA//PycharmProjects//DOMFRMWRKEX'):
        filename=self.filename_generator(prefix,extension)
        FolderName=self.create_Folder(path,FolderName)
        screenshot_location=os.path.join(FolderName,filename)
        print(screenshot_location)
        return screenshot_location

        # self.driver.save_screenshot(screenshot_location)


ff=Take_Screenshot()
ff.Take_Screenshot(prefix='scrnsht',extension='.png',FolderName='screenshots',path='C:\\Users\\MEGHA\\PycharmProjects\\DOMFRMWRKEX')


