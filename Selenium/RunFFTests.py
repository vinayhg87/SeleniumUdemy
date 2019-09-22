from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

from selenium.webdriver import ActionChains


class FFtest(object):
    def testMethod(self):
        # os.getcwd() will fetch the current working directory
        gekodriverPath = os.getcwd() + "/Drivers/geckodriver.exe"
        # initiating web-driver instance
        driver = webdriver.Firefox(executable_path=gekodriverPath)
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.find_element_by_id("bmwcheck")







obj = FFtest()
obj.testMethod()
