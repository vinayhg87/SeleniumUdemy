# https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
#from pywinauto import keyboard
import os
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
import configparser

logging.basicConfig(filename="selenium.log", level="DEBUG")
logging.warning("Test message")

parser = configparser.RawConfigParser()
parser.read(os.getcwd()+"/DBDetails.properties")
hostname = parser.get("BSCSDB", "hostname")
port = parser.get("BSCSDB", "port")
logging.info("The host and port of DB is %s and %s" % (hostname, port))

class FFtest(object):
    def testMethod(self):
        # os.getcwd() will fetch the current working directory
        browser = input("Select the browser FF or CH \n")
        driver = None
        # FireFox browser
        if browser == "FF":
            gekodriverpath = os.getcwd() + "/Drivers/geckodriver.exe"
            driver = webdriver.Firefox(executable_path=gekodriverpath)
        # Chrome browser
        elif browser == "CH":
            chromedriverpath = os.getcwd() + "/Drivers/chromedriver.exe"
            driver = webdriver.Chrome(executable_path=chromedriverpath)
        # initiating web-driver instance

        try:
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://learn.letskodeit.com/p/practice")

            # this is javascript execution
            # driver.execute_script("window.location = 'https://www.google.com';")  # to open the web-page.
            # driver.execute_script("return document.getElementById("ID")")  # finding element using java script
            # driver.execute_script("window.scrollBy(0,1000);")  # to scroll down using java script
            # driver.execute_script("window.scrollBy(0,-1000);")  # to scroll down using java script

            # Getting size of window using javascript
            height = driver.execute_script("return window.innerHeight;")
            width = driver.execute_script("return window.innerWidth;")
            print("height is %d" % height)
            print("width is %d" % width)

            driver.find_element_by_id("bmwradio").click()
            # web-element state
            print(driver.find_element_by_id("bmwradio").is_displayed())
            print(driver.find_element_by_id("bmwradio").is_enabled())
            print(driver.find_element_by_id("bmwradio").is_selected())
            # Radio Button Example
            driver.find_element(By.ID, "bmwradio").click()  # this will also work but it is just an example.
            # list of radio buttons being fetched in the below command.
            RadioButtonList = driver.find_elements_by_xpath("//fieldset/label/input[@type='radio']")
            for btn in RadioButtonList:
                btn.click()  # Clicking the radio button in loop
                print(btn.get_attribute("value"))

            # Select Class Example
            dropdownList = driver.find_element_by_xpath("//fieldset/select[@id='carselect']")
            select = Select(dropdownList)
            for opt in select.options:
                if opt.text == "Honda":
                    select.select_by_visible_text(opt.text)

            for index in range(len(select.options)):
                select.select_by_index(index)

            # Select class with multi select
            multidropdownList = driver.find_element_by_xpath("//fieldset/select[@id='multiple-select-example']")
            select = Select(multidropdownList)

            # multi select
            for opt in select.options:
                select.select_by_visible_text(opt.text)

            # Checkbox Example
            checkboxList = driver.find_elements_by_xpath("//input[@type='checkbox']")
            for checkbox in checkboxList:
                checkbox.click()

            # switch tab Example (Same logic as switch-to window)
            currenttab = driver.window_handles[0]
            driver.find_element_by_id("opentab").click()
            time.sleep(1)
            windowHandles = driver.window_handles
            for x in range(len(windowHandles)):
                if currenttab not in windowHandles[x]:
                    driver.switch_to.window(windowHandles[x])
                    time.sleep(2)
                    driver.find_element_by_id("search-courses").send_keys("Test2")
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(currenttab)
                    time.sleep(2)

            # Switch Window Example
            baseWindow = driver.window_handles[0]
            driver.find_element_by_id("openwindow").click()
            size = len(driver.window_handles)
            for win in range(size):
                if baseWindow not in driver.window_handles[win]:
                    driver.switch_to.window(driver.window_handles[win])
                    time.sleep(2)
                    driver.find_element_by_id("search-courses").send_keys("Test1")
                    time.sleep(2)
                    driver.close()
                    time.sleep(2)
                    driver.switch_to.window(baseWindow)

            # Switch-to alert Example
            time.sleep(1)
            driver.find_element_by_name("enter-name").send_keys("Hello World")
            time.sleep(2)
            driver.find_element_by_css_selector("input[value^='Alert']").click()
            time.sleep(1)
            wait = WebDriverWait(driver,10)
            wait.until(expected_conditions.alert_is_present())
            AlertPrompt = driver.switch_to.alert
            print("Data fetched from Alert is : "+AlertPrompt.text)
            AlertPrompt.accept()
            time.sleep(2)

            # keyboard Actions. Pressing page down
            #keyboard.send_keys("{PGDN}")
            #keyboard.send_keys("{PGDN}")

            # I-frame Example
            iframewindow = driver.find_element(By.ID, "courses-iframe")
            driver.switch_to.frame(iframewindow)
            time.sleep(2)
            driver.find_element(By.ID, "search-courses").send_keys("python")
            time.sleep(3)
            driver.switch_to.default_content()

            # keyboard Actions. Pressing page up
            #keyboard.send_keys("{PGUP}")

            # Element Displayed Example
            driver.find_element(By.ID, "show-textbox").click()
            time.sleep(3)
            driver.find_element(By.ID, "displayed-text").send_keys("Hello World")

            # taking screenshots
            driver.get_screenshot_as_file(os.getcwd()+"/ScreenShots/test1.png")

        except Exception as e:
            print("Exception occurred : " + str(e))

        finally:
                print("Closing the current browser")
                driver.close()



obj = FFtest()
obj.testMethod()
