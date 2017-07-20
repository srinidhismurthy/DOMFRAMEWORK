from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as CL
import os
import time
from selenium.webdriver.support.select import Select


class MyDriver():

    log=CL.fileLogger()

    def __init__(self,driver):
        self.driver=driver


    # def startDriver(self,baseURL):
    #     self.driver.maximize_window()
    #     self.driver.get(baseURL)
    #     self.driver.implicitly_wait(5)
    #     return self.driver

    # Variable
    _windows_scroller="window.scrollBy(0,{0});"

    def scrollup(self,scroll_value):
        _scroll_value = -(int(str(scroll_value)))
        self.driver.execute_script(self._windows_scroller.format(_scroll_value))

    def scrolldown(self,scroll_value):
        self.driver.execute_script(self._windows_scroller.format(scroll_value))

    def getIDType(self, locatorType):

        locatorType= locatorType.lower()

        if locatorType=="id":
            return By.ID

        if locatorType =="xpath":
            return By.XPATH

        if locatorType == "link text":
            return By.LINK_TEXT

        if locatorType == "partial link text":
            return By.PARTIAL_LINK_TEXT

        if locatorType =="name":
            return By.NAME

        if locatorType == "tag name":
            return By.TAG_NAME

        if locatorType == "class name":
            return By.CLASS_NAME

        if locatorType == "css selector":
            return By.CSS_SELECTOR

    def getElement(self,locatorType='id',locator=''):
        element=None
        try:
            byType=self.getIDType(locatorType)
            element=self.driver.find_element(byType,locator)
        except:
            print("Element with "+str( locator)+ "could not be found")

        return element

    def clickElement(self,locatorType,locator):

        element=self.getElement(locatorType,locator,)
        element.click()
        self.log.info("The element with locator"+str(locator)+
                         'and LocatorType '+str(locatorType)+'is clicked')

    def sendData(self,data,locator,locatorType,):
        element=self.getElement(locatorType,locator)
        print("found element")
        element.clear()
        element.send_keys(data)
        self.log.info("The element with locator"+str(locator)+'and LocatorType '
                      +str(locatorType)+'has recieved'+str(data))
        return element

    def sendData_No_clear(self,data,locator,locatorType,):
        element=self.getElement(locator,locatorType)
        print("found element")
        element.send_keys(data)
        self.log.info("The element with locator"+str(locator)+'and LocatorType '
                      +str(locatorType)+'has recieved'+str(data))
        return element

    def select_option(self,locator,locatorType,select_by_type,select_by_entry):

        select_by_type=select_by_type.lower()

        element=self.getElement(locator,locatorType)
        sel=Select(element)

        if select_by_type=='value':
            sel.select_by_value(select_by_entry)
        if select_by_type=='index':
            sel.select_by_index(select_by_entry)
        if select_by_type=='visible text':
            sel.select_by_visible_text(select_by_entry)

    def explicitWait(self,locatorType,locator):

        # locatorType=locatorType.lower()
        wait=WebDriverWait(self.driver,3,1,ignored_exceptions=[NoSuchElementException,
                           ElementNotVisibleException,ElementNotSelectableException,TimeoutException])

        element=wait.until(EC.element_to_be_clickable((locatorType,locator)))
        self.log.info("Explicit wait condition worked on "
                          "element with locator "+str(locator))
        return element

    def elemAssert(self,locatorType,locator):

        try:
            element=self.explicitWait(locatorType,locator)
            assert element != None
            self.log.info("******** ASSERTION PASSED ***********")
        except:
            self.log.error("!!!!!!!!!! ASSERTION FAILED for element with locator type {}"
                  " could not be found!!!!!!!!!!!".format(locator))

    def iselementpresent(self,locatorType,locator):

        element=self.getElement(locator,locatorType)
        if element is not None:
            print("Element is present")
            return True
        else:
            print("Element is not preset")
            return False

    def new_Assert_check(self,locatorType,locator):

        try:
            element=self.explicitWait(locatorType,locator)
            assert element !=None
            print("Assertion Element found")
            return True
        except:
            print('Could not find the Assertion element')
            return False

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
            print("path already exists with {}".format(new_folder))
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

    def filename_generator(self,prefix,extension,path,folderName):

        filename_generator=str(round(time.time()*1000))
        slice_5letter=filename_generator[:6]
        file_name=prefix+'_'+slice_5letter+extension

        return file_name

    def Take_Screenshot(self,prefix='scrnsht',extension='.png',FolderName='screenshots',path='C://Users//MEGHA//PycharmProjects//DOMFRMWRKEX'):
        filename=self.filename_generator(prefix,extension,path,FolderName)
        FolderName=self.create_Folder(path,FolderName)
        screenshot_location=os.path.join(FolderName,filename)

        self.driver.save_screenshot(screenshot_location)



