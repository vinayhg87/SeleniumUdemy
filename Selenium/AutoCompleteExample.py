from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AutoComplete(object):
    def test1(self):
        driver = None
        try:
            driver = webdriver.Firefox()
            driver.get("https://www.google.co.in/")
            driver.maximize_window()
            driver.find_element(By.NAME, "q").send_keys("hello")
            time.sleep(1)

            suggestionListbox = driver.find_elements(By.XPATH, "//ul[@role='listbox']//div/*[@role='option']//span")
            for listInfo in suggestionListbox:
                print(listInfo.text)
            driver.get_screenshot_as_file(os.getcwd()+"/ScreenShots/AutoComplete1.png")
            # Clicking the 3 option in the list
            suggestionListbox[3].click()
            driver.get_screenshot_as_file(os.getcwd() + "/ScreenShots/AutoComplete2.png")

        except Exception as e:
            print(str(e))

        finally:
            if driver is not None:
                driver.close()


obj = AutoComplete()
obj.test1()