from selenium import webdriver
import os

class ChromeTests(object):
    def testMethod(self):
        # os.getcwd() will fetch the current working directory
        chromedriverPath = os.getcwd()+"\Drivers\chromedriver.exe"
        print(chromedriverPath)
        driver = webdriver.Chrome(executable_path=chromedriverPath)
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")


obj = ChromeTests()
obj.testMethod()