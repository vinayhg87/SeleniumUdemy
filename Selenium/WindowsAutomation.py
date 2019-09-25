from selenium import webdriver
from pywinauto import keyboard
import time
import os


class winAutomation(object):
    def winAuto(self):
        gekodriverpath = os.getcwd() + "/Drivers/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=gekodriverpath)
        driver.get("https://www.seleniumhq.org/download/")
        driver.find_element_by_xpath("//a[contains(text(),'3.141.59')]").click()
        time.sleep(2)
        keyboard.send_keys("{ENTER}")
        driver.quit()


obj = winAutomation()
obj.winAuto()