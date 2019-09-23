from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import os


class FFtest(object):
    def testMethod(self):
        # os.getcwd() will fetch the current working directory
        gekodriverPath = os.getcwd() + "/Drivers/geckodriver.exe"
        # initiating web-driver instance
        driver = webdriver.Firefox(executable_path=gekodriverPath)
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

            for opt in select.options:
                select.select_by_visible_text(opt.text)

            # Checkbox Example
            driver.find_element_by_id("bmwcheck").click()
            driver.find_element_by_id("benzcheck").click()
            driver.find_element_by_id("hondacheck").click()

        except Exception as e:
            print("Exception occurred : " + str(e))

        finally:
            print("Closing the current browser")
            driver.close()


obj = FFtest()
obj.testMethod()
