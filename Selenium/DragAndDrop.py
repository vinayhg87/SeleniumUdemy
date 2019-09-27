from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

class DragDropExample():
    def test1(self):
        driver = webdriver.Firefox()
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)
        driver.switch_to.frame(0)
        dragElement = driver.find_element(By.ID, "draggable")
        dropElement = driver.find_element(By.ID, "droppable")
        action = ActionChains(driver)
        time.sleep(2)
        #action.drag_and_drop(dragElement, dropElement).perform()
        # or
        action.click_and_hold(dragElement).move_to_element(dropElement).release().perform()
        time.sleep(2)
        driver.get_screenshot_as_file(os.getcwd()+"/ScreenShots/dragdrop.png")
        driver.switch_to.default_content()
        driver.close()


obj = DragDropExample()
obj.test1()