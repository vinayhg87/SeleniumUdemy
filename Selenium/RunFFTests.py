from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import os
import time


class FFtest(object):
    def testMethod(self):
        # os.getcwd() will fetch the current working directory
        browser = input("Select the browser FF or CH \n")
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
            driver.maximize_window()
            driver.get("https://learn.letskodeit.com/p/practice")
            driver.find_element_by_id("bmwradio").click()
            # Radio Button Example
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

            # Switch Window
            baseWindow = driver.window_handles[0]
            driver.find_element_by_id("openwindow").click()
            size = len(driver.window_handles)
            for win in range(size):
                if baseWindow != driver.window_handles[win]:
                    driver.switch_to.window(driver.window_handles[win])
                    time.sleep(2)
                    driver.find_element_by_id("search-courses").send_keys("Test1")
                    time.sleep(2)
                    driver.close()
                    time.sleep(2)
                    driver.switch_to.window(baseWindow)

            # Switch-to alert Example
            time.sleep(2)
            driver.find_element_by_name("enter-name").send_keys("Hello World")
            time.sleep(2)
            driver.find_element_by_css_selector("input[value^='Alert']").click()
            time.sleep(1)
            Alertprompt = driver.switch_to.alert
            print("Data fetched from Alert is : "+Alertprompt.text)
            Alertprompt.accept()
            time.sleep(2)


        except Exception as e:
            print("Exception occurred : " + str(e))

        finally:
                print("Closing the current browser")
                driver.close()



obj = FFtest()
obj.testMethod()
